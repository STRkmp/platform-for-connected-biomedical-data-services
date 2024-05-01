import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class Attention_block(nn.Module):
    """
    Attention Block
    """

    def __init__(self, F_g, F_l, F_int):
        super(Attention_block, self).__init__()

        self.W_g = nn.Sequential(
            nn.Conv2d(F_l, F_int, kernel_size=1, stride=1, padding=0, bias=True),
            nn.BatchNorm2d(F_int)
        )

        self.W_x = nn.Sequential(
            nn.Conv2d(F_g, F_int, kernel_size=1, stride=1, padding=0, bias=True),
            nn.BatchNorm2d(F_int)
        )

        self.psi = nn.Sequential(
            nn.Conv2d(F_int, 1, kernel_size=1, stride=1, padding=0, bias=True),
            nn.BatchNorm2d(1),
            nn.Sigmoid()
        )

        self.relu = nn.ReLU(inplace=True)

    def forward(self, g, x):
        g1 = self.W_g(g)
        x1 = self.W_x(x)
        psi = self.relu(g1 + x1)
        psi = self.psi(psi)
        out = x * psi
        return out


class AttU_Net(nn.Module):
    def __init__(self):
        super().__init__()

        # encoder (downsampling)
        # 256 -> 128
        prob = 0.6
        activate_f = nn.ReLU()

        self.encoder_0 = nn.Sequential(
            nn.Conv2d(1, 64, 3, 1, 1),
            nn.BatchNorm2d(64),
            activate_f,
            nn.Conv2d(64, 64, 3, 1, 1),
            nn.BatchNorm2d(64),
            # nn.ReLU(),
            activate_f
        )

        # 128 -> 64
        self.encoder_1 = nn.Sequential(
            nn.Dropout(p=prob),
            nn.Conv2d(64, 128, 3, 1, 1),
            nn.BatchNorm2d(128),
            activate_f,
            nn.Conv2d(128, 128, 3, 1, 1),
            nn.BatchNorm2d(128),
            # nn.ReLU(),
            activate_f
        )

        # 64 -> 32
        self.encoder_2 = nn.Sequential(
            nn.Dropout(p=prob),
            nn.Conv2d(128, 256, 3, 1, 1),
            nn.BatchNorm2d(256),
            activate_f,
            nn.Conv2d(256, 256, 3, 1, 1),
            nn.BatchNorm2d(256),
            activate_f
        )

        # 32 -> 16
        self.encoder_3 = nn.Sequential(
            nn.Dropout(p=prob),
            nn.Conv2d(256, 512, 3, 1, 1),
            nn.BatchNorm2d(512),
            activate_f,
            nn.Conv2d(512, 512, 3, 1, 1),
            nn.BatchNorm2d(512),
            activate_f,
        )

        self.bottleneck = nn.Sequential(
            nn.Dropout(p=prob),
            nn.Conv2d(512, 1024, 3, 1, 1),
            nn.BatchNorm2d(1024),
            activate_f,
            nn.Conv2d(1024, 512, 3, 1, 1),
            nn.BatchNorm2d(512),
            activate_f
        )

        # decoder (upsampling)
        # 16 -> 32
        self.decoder_0 = nn.Sequential(
            nn.Dropout(p=prob),
            nn.Conv2d(1024, 512, 3, 1, 1),
            nn.BatchNorm2d(512),
            activate_f,
            nn.Conv2d(512, 256, 3, 1, 1),
            nn.BatchNorm2d(256),
            activate_f,
        )

        # 32 -> 64
        self.decoder_1 = nn.Sequential(
            nn.Dropout(p=prob),
            nn.Conv2d(512, 256, 3, 1, 1),
            nn.BatchNorm2d(256),
            activate_f,
            nn.Conv2d(256, 128, 3, 1, 1),
            nn.BatchNorm2d(128),
            activate_f
        )

        # 64 -> 128
        self.decoder_2 = nn.Sequential(
            nn.Dropout(p=prob),
            nn.Conv2d(256, 128, 3, 1, 1),
            nn.BatchNorm2d(128),
            activate_f,
            nn.Conv2d(128, 64, 3, 1, 1),
            nn.BatchNorm2d(64),
            activate_f,
        )

        # 128 -> 256
        self.decoder_3 = nn.Sequential(
            nn.Dropout(p=prob),
            nn.Conv2d(128, 64, 3, 1, 1),
            nn.BatchNorm2d(64),
            activate_f,
            nn.Conv2d(64, 64, 3, 1, 1),
            nn.BatchNorm2d(64),
            activate_f,
            nn.Conv2d(64, 1, 3, 1, 1),  # по схеме выход должен быть равен 2 + 1*1, а не 3*3
            nn.Sigmoid()
        )

        self.pool = nn.MaxPool2d(2, 2)
        self.upsample = nn.Upsample(scale_factor=2, mode='nearest')

        n1 = 64
        filters = [n1, n1 * 2, n1 * 4, n1 * 8, n1 * 16]
        self.Att5 = Attention_block(F_g=filters[3], F_l=filters[3], F_int=filters[2])
        self.Att4 = Attention_block(F_g=filters[2], F_l=filters[2], F_int=filters[1])
        self.Att3 = Attention_block(F_g=filters[1], F_l=filters[1], F_int=filters[0])
        self.Att2 = Attention_block(F_g=filters[0], F_l=filters[0], F_int=32)

    def forward(self, x):
        # encoder
        e0 = self.encoder_0(x)
        e0_pool = self.pool(e0)
        e1 = self.encoder_1(e0_pool)
        e1_pool = self.pool(e1)
        e2 = self.encoder_2(e1_pool)
        e2_pool = self.pool(e2)
        e3 = self.encoder_3(e2_pool)
        e3_pool = self.pool(e3)

        # bottleneck
        b = self.bottleneck(e3_pool)

        b_up = self.upsample(b)
        a_1 = self.Att5(g=b_up, x=e3)

        # decoder
        d0 = self.decoder_0(torch.cat([a_1, b_up], 1))

        b_2_up = self.upsample(d0)
        a_2 = self.Att4(g=b_2_up, x=e2)
        d1 = self.decoder_1(torch.cat([a_2, b_2_up], 1))

        b_3_up = self.upsample(d1)
        a_3 = self.Att3(g=b_3_up, x=e1)
        d2 = self.decoder_2(torch.cat([a_3, b_3_up], 1))

        b_4_up = self.upsample(d2)
        a_4 = self.Att2(g=b_4_up, x=e0)
        d3 = self.decoder_3(torch.cat([self.upsample(d2), e0], 1))

        return d3