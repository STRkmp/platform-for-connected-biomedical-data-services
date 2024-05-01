from diplom_backend.service.report import make_report


def make_report(ct, mask, data_for_report):
    mask = mask.numpy()
    ct = ct.numpy()
    doc_gen = make_report(ct, mask, data_for_report)
    return doc_gen.convert_to_pdf()
