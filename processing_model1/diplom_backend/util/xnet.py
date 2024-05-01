import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


class XNet(nn.Module):
    def __init__(self):
        super().__init__()

        activation_f = nn.ReLU()
        self.pool = nn.MaxPool2d(2, 2)
        self.upsample = nn.Upsample(scale_factor=2, mode='nearest')

        self.encoder_1 = nn.Sequential(
            nn.Conv2d(1, 64, 3, 1, 1),
            nn.BatchNorm2d(64),
            activation_f,
        )

        self.encoder_2 = nn.Sequential(
            nn.Conv2d(64, 128, 3, 1, 1),
            nn.BatchNorm2d(128),
            activation_f,
        )

        self.encoder_3 = nn.Sequential(
            nn.Conv2d(128, 256, 3, 1, 1),
            nn.BatchNorm2d(256),
            activation_f,
        )

        # flat
        self.encoder_4 = nn.Sequential(
            nn.Conv2d(256, 512, 3, 1, 1),
            nn.BatchNorm2d(512),
            activation_f,

            nn.Conv2d(512, 512, 3, 1, 1),
            nn.BatchNorm2d(512),
            activation_f
        )

        # up
        self.decoder_0 = nn.Sequential(
            nn.Conv2d(512, 256, 3, 1, 1),
            nn.BatchNorm2d(256),
            activation_f,
        )

        self.decoder_1 = nn.Sequential(
            nn.Conv2d(512, 128, 3, 1, 1),
            nn.BatchNorm2d(128),
            activation_f,
        )

        # down
        self.decoder_2 = nn.Sequential(
            # 256 -> 256
            nn.Conv2d(256, 128, 3, 1, 1),
            nn.BatchNorm2d(128),
            activation_f,
        )

        self.decoder_3 = nn.Sequential(
            nn.Conv2d(128, 256, 3, 1, 1),
            nn.BatchNorm2d(256),
            activation_f,
        )

        # flat
        self.decoder_4 = nn.Sequential(
            nn.Conv2d(256, 512, 3, 1, 1),
            nn.BatchNorm2d(512),
            activation_f,

            nn.Conv2d(512, 512, 3, 1, 1),
            nn.BatchNorm2d(512),
            activation_f,
        )

        self.decoder_6 = nn.Sequential(
            nn.Conv2d(512, 256, 3, 1, 1),
            nn.BatchNorm2d(256),
            activation_f,
        )

        self.decoder_7 = nn.Sequential(
            nn.Conv2d(512, 128, 3, 1, 1),
            nn.BatchNorm2d(128),
            activation_f,
        )

        self.decoder_8 = nn.Sequential(
            nn.Conv2d(256, 64, 3, 1, 1),
            nn.BatchNorm2d(64),
            activation_f,
        )

        self.conv_0 = nn.Sequential(
            nn.Conv2d(128, 1, 3, 1, 1),
            nn.BatchNorm2d(1),
            nn.Sigmoid()
        )

    def forward(self, x):
        # encoder
        e0 = self.encoder_1(x)
        e0_pool = self.pool(e0)

        e1 = self.encoder_2(e0_pool)
        e1_pool = self.pool(e1)
        e2 = self.encoder_3(e1_pool)
        e2_pool = self.pool(e2)

        # flat
        e3 = self.encoder_4(e2_pool)

        # up
        u0 = torch.cat([e2, self.decoder_0(self.upsample(e3))], 1)
        u1 = torch.cat([e1, self.decoder_1(self.upsample(u0))], 1)

        # Down
        d0 = self.decoder_2(u1)
        d0_pool = self.pool(d0)
        d1 = self.decoder_3(d0_pool)
        d1_pool = self.pool(d1)

        # flat
        f3 = self.decoder_4(d1_pool)

        # encoder
        e4 = torch.cat([d1, self.decoder_6(self.upsample(f3))], 1)
        e5 = torch.cat([d0, self.decoder_7(self.upsample(e4))], 1)
        e6 = torch.cat([e0, self.decoder_8(self.upsample(e5))], 1)

        conv0 = self.conv_0(e6)  # padding = valid

        return conv0
