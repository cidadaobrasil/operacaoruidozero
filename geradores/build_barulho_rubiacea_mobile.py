from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import portrait
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    Frame,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


# O PDF sai ao lado deste script, em geradores/pdf/. Antes daqui havia um
# caminho absoluto ("C:\projetos\Sites basicos"), que so funcionava nesta
# maquina e neste lugar do disco: mover a pasta ou abrir em outro PC quebrava.
ROOT = Path(__file__).resolve().parent
OUT = ROOT / "pdf" / "guia-barulho-casa-vizinha-rubiacea-mobile.pdf"
PAGE_W, PAGE_H = 390, 844
MARGIN_X = 24
TOP_MARGIN = 28
BOTTOM_MARGIN = 26


def register_fonts():
    fonts = {
        "Arial": Path(r"C:\Windows\Fonts\arial.ttf"),
        "Arial-Bold": Path(r"C:\Windows\Fonts\arialbd.ttf"),
    }
    if all(path.exists() for path in fonts.values()):
        for name, path in fonts.items():
            pdfmetrics.registerFont(TTFont(name, str(path)))
        return "Arial", "Arial-Bold"
    return "Helvetica", "Helvetica-Bold"


FONT, BOLD = register_fonts()


PALETTE = {
    "ink": colors.HexColor("#263238"),
    "muted": colors.HexColor("#5F6B77"),
    "paper": colors.HexColor("#FFFFFF"),
    "line": colors.HexColor("#DCE3EA"),
    "red": colors.HexColor("#E22B2F"),
    "orange": colors.HexColor("#F47C00"),
    "blue": colors.HexColor("#1E73BE"),
    "purple": colors.HexColor("#9235AF"),
    "amber": colors.HexColor("#F1B700"),
    "green": colors.HexColor("#2B9B47"),
    "navy": colors.HexColor("#1E568A"),
    "violet_bg": colors.HexColor("#F5F0FF"),
    "green_bg": colors.HexColor("#EFFAF1"),
    "yellow_bg": colors.HexColor("#FFF8E5"),
    "blue_bg": colors.HexColor("#EEF6FF"),
    "soft": colors.HexColor("#F8FAFC"),
}


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="BodyMobile",
        parent=styles["BodyText"],
        fontName=FONT,
        fontSize=13,
        leading=17.2,
        textColor=PALETTE["ink"],
        spaceAfter=6,
    )
)
styles.add(
    ParagraphStyle(
        name="SmallMobile",
        parent=styles["BodyMobile"],
        fontSize=10.8,
        leading=14.4,
        textColor=PALETTE["muted"],
        spaceAfter=4,
    )
)
styles.add(
    ParagraphStyle(
        name="TitleMobile",
        parent=styles["BodyMobile"],
        fontName=BOLD,
        fontSize=25,
        leading=28,
        textColor=colors.white,
        spaceAfter=6,
    )
)
styles.add(
    ParagraphStyle(
        name="SubtitleMobile",
        parent=styles["BodyMobile"],
        fontName=FONT,
        fontSize=12.6,
        leading=16,
        textColor=colors.white,
        spaceAfter=4,
    )
)
styles.add(
    ParagraphStyle(
        name="SectionTitle",
        parent=styles["BodyMobile"],
        fontName=BOLD,
        fontSize=14.2,
        leading=17,
        textColor=PALETTE["ink"],
        spaceAfter=8,
    )
)
styles.add(
    ParagraphStyle(
        name="CardTitle",
        parent=styles["BodyMobile"],
        fontName=BOLD,
        fontSize=16.4,
        leading=20,
        textColor=PALETTE["ink"],
        spaceAfter=8,
    )
)
styles.add(
    ParagraphStyle(
        name="ContactTitle",
        parent=styles["BodyMobile"],
        fontName=BOLD,
        fontSize=11.2,
        leading=14,
        textColor=colors.white,
        spaceAfter=4,
    )
)
styles.add(
    ParagraphStyle(
        name="ContactNumber",
        parent=styles["BodyMobile"],
        fontName=BOLD,
        fontSize=20,
        leading=23,
        textColor=colors.HexColor("#FFE15A"),
        spaceAfter=2,
    )
)
styles.add(
    ParagraphStyle(
        name="ContactNote",
        parent=styles["BodyMobile"],
        fontName=FONT,
        fontSize=10.8,
        leading=14.4,
        textColor=colors.HexColor("#EAF3FF"),
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="ContactTitleMini",
        parent=styles["BodyMobile"],
        fontName=BOLD,
        fontSize=8.7,
        leading=10.8,
        textColor=colors.white,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="ContactNumberMini",
        parent=styles["BodyMobile"],
        fontName=BOLD,
        fontSize=15.6,
        leading=18,
        textColor=colors.HexColor("#FFE15A"),
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="ContactNoteMini",
        parent=styles["BodyMobile"],
        fontName=FONT,
        fontSize=8.4,
        leading=10.6,
        textColor=colors.HexColor("#EAF3FF"),
        spaceAfter=0,
    )
)


def esc(text):
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\n", "<br/>")
    )


def p(text, style="BodyMobile"):
    return Paragraph(text, styles[style])


def bullet(text):
    return Paragraph(f"&bull;&nbsp;&nbsp;{text}", styles["BodyMobile"])


def callout(text, color):
    table = Table([[Paragraph(text, styles["BodyMobile"])]], colWidths=[None])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.white),
                ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#D8E1EA")),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                ("ROUNDEDCORNERS", (0, 0), (-1, -1), 7),
            ]
        )
    )
    return table


class Hero(Flowable):
    def __init__(self):
        super().__init__()
        self.height = 176

    def wrap(self, avail_width, avail_height):
        return avail_width, self.height

    def draw(self):
        c = self.canv
        c.saveState()
        c.translate(-MARGIN_X, 0)
        c.setFillColor(PALETTE["red"])
        c.rect(0, 0, PAGE_W, self.height, stroke=0, fill=1)
        c.setFillColor(PALETTE["orange"])
        c.rect(PAGE_W * 0.52, 0, PAGE_W * 0.48, self.height, stroke=0, fill=1)
        c.setFillColor(colors.Color(1, 1, 1, alpha=0.18))
        c.roundRect(24, self.height - 42, 118, 22, 11, stroke=1, fill=0)
        c.setFillColor(colors.white)
        c.setFont(BOLD, 8.5)
        c.drawString(38, self.height - 35, "GUIA DO MORADOR")
        c.setFont(BOLD, 25)
        c.drawString(24, self.height - 72, "Barulho em casa")
        c.drawString(24, self.height - 102, "vizinha: o que fazer?")
        c.setFont(FONT, 12)
        c.drawString(24, self.height - 130, "Passo a passo para lidar com")
        c.drawString(24, self.height - 146, "perturbação do sossego")
        c.setFillColor(colors.Color(0, 0, 0, alpha=0.16))
        c.roundRect(24, 8, 288, 26, 8, stroke=0, fill=1)
        c.setFillColor(colors.white)
        c.setFont(BOLD, 9.2)
        c.drawString(40, 18, "Guia elaborado para os moradores de Rubiácea/SP")
        c.restoreState()


class SectionCard(Flowable):
    def __init__(self, number, color, title, flows):
        super().__init__()
        self.number = str(number)
        self.color = color
        self.title = title
        self.flows = [p(esc(title), "CardTitle")] + flows
        self.width = 0
        self.height = 0
        self.measurements = []

    def wrap(self, avail_width, avail_height):
        self.width = avail_width
        inner_width = avail_width - 78
        total = 22
        self.measurements = []
        for flow in self.flows:
            w, h = flow.wrap(inner_width, avail_height)
            self.measurements.append((flow, w, h))
            total += h + 2
        self.height = max(total + 18, 118)
        return avail_width, self.height

    def draw(self):
        c = self.canv
        c.saveState()
        c.setFillColor(colors.white)
        c.setStrokeColor(PALETTE["line"])
        c.roundRect(0, 0, self.width, self.height, 8, stroke=1, fill=1)
        c.setFillColor(self.color)
        c.roundRect(0, 0, 48, self.height, 8, stroke=0, fill=1)
        c.rect(40, 0, 8, self.height, stroke=0, fill=1)
        c.setFillColor(colors.white)
        c.setFont(BOLD, 22)
        c.drawCentredString(24, self.height / 2 - 7, self.number)
        y = self.height - 20
        x = 66
        for flow, w, h in self.measurements:
            y -= h
            flow.drawOn(c, x, y)
            y -= 2
        c.restoreState()


class PlainCard(Flowable):
    def __init__(self, title, flows, bg, border, title_color=None):
        super().__init__()
        self.title = title
        self.flows = [p(title, "CardTitle")] + flows if title else flows
        self.bg = bg
        self.border = border
        self.title_color = title_color
        self.width = 0
        self.height = 0
        self.measurements = []

    def wrap(self, avail_width, avail_height):
        self.width = avail_width
        inner_width = avail_width - 28
        total = 18
        self.measurements = []
        for flow in self.flows:
            w, h = flow.wrap(inner_width, avail_height)
            self.measurements.append((flow, w, h))
            total += h + 3
        self.height = total + 18
        return avail_width, self.height

    def draw(self):
        c = self.canv
        c.saveState()
        c.setFillColor(self.bg)
        c.setStrokeColor(self.border)
        c.roundRect(0, 0, self.width, self.height, 8, stroke=1, fill=1)
        y = self.height - 18
        for flow, w, h in self.measurements:
            y -= h
            flow.drawOn(c, 14, y)
            y -= 3
        c.restoreState()


def contact_card(title, number, note):
    data = [
        [Paragraph(title, styles["ContactTitle"])],
        [Paragraph(number, styles["ContactNumber"])],
        [Paragraph(note, styles["ContactNote"])],
    ]
    table = Table(data, colWidths=[342 - 28])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.Color(1, 1, 1, alpha=0.12)),
                ("BOX", (0, 0), (-1, -1), 0.5, colors.Color(1, 1, 1, alpha=0.24)),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                ("TOPPADDING", (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
                ("ROUNDEDCORNERS", (0, 0), (-1, -1), 7),
            ]
        )
    )
    return table


class CompactContactsCard(Flowable):
    def __init__(self):
        super().__init__()
        self.height = 244
        self.width = 0
        self.rows = [
            (
                "5ª Companhia da Polícia Militar - Guararapes/SP",
                "(18) 3606-1347",
                ["NUMEC - Núcleo de Mediação Comunitária", "Cb PM Jurca · Subten PM Marcos"],
                66,
            ),
            (
                "Prefeitura Municipal de Rubiácea/SP",
                "(18) 3697-9117",
                ["Providências administrativas e fiscalização municipal"],
                55,
            ),
            ("Emergência", "190", ["Polícia Militar"], 57),
        ]

    def wrap(self, avail_width, avail_height):
        self.width = avail_width
        return avail_width, self.height

    def draw(self):
        c = self.canv
        c.saveState()
        c.setFillColor(PALETTE["navy"])
        c.roundRect(0, 0, self.width, self.height, 8, stroke=0, fill=1)
        c.setFillColor(colors.white)
        c.setFont(BOLD, 13.2)
        c.drawCentredString(self.width / 2, self.height - 25, "CONTATOS ÚTEIS")

        y = self.height - 46
        for title, number, notes, row_h in self.rows:
            c.setFillColor(colors.HexColor("#3D74A1"))
            c.roundRect(12, y - row_h, self.width - 24, row_h, 4, stroke=0, fill=1)
            c.setFillColor(colors.Color(1, 1, 1, alpha=0.20))
            c.setStrokeColor(colors.Color(1, 1, 1, alpha=0.22))
            c.roundRect(12, y - row_h, self.width - 24, row_h, 4, stroke=1, fill=0)

            x = 24
            c.setFillColor(colors.white)
            c.setFont(BOLD, 8.8)
            c.drawString(x, y - 17, title)
            c.setFillColor(colors.HexColor("#FFE15A"))
            c.setFont(BOLD, 15.8)
            c.drawString(x, y - 39, number)
            c.setFillColor(colors.HexColor("#EAF3FF"))
            c.setFont(FONT, 8.8)
            note_y = y - (46 if title == "Emergência" else 53)
            for note in notes:
                c.drawString(x, note_y, note)
                note_y -= 11
            y -= row_h + 7
        c.restoreState()


def top_bar(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(PALETTE["navy"])
    canvas.rect(0, PAGE_H - 38, PAGE_W, 38, stroke=0, fill=1)
    canvas.setFillColor(colors.white)
    canvas.setFont(BOLD, 8.5)
    canvas.drawString(MARGIN_X, PAGE_H - 24, "GUIA DO MORADOR")
    canvas.setFont(FONT, 8.5)
    canvas.drawRightString(PAGE_W - MARGIN_X, PAGE_H - 24, f"{doc.page}")
    canvas.restoreState()


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(colors.HexColor("#AEB7C2"))
    canvas.setFont(FONT, 8)
    canvas.drawCentredString(PAGE_W / 2, 17, "Guia informativo elaborado para a comunidade de Rubiácea/SP - compartilhe com seus vizinhos.")
    canvas.restoreState()


def later_page(canvas, doc):
    top_bar(canvas, doc)
    footer(canvas, doc)


def first_page(canvas, doc):
    footer(canvas, doc)


def build():
    doc = BaseDocTemplate(
        str(OUT),
        pagesize=portrait((PAGE_W, PAGE_H)),
        leftMargin=MARGIN_X,
        rightMargin=MARGIN_X,
        topMargin=TOP_MARGIN,
        bottomMargin=BOTTOM_MARGIN,
    )
    frame = Frame(
        doc.leftMargin,
        doc.bottomMargin,
        PAGE_W - 2 * MARGIN_X,
        PAGE_H - TOP_MARGIN - BOTTOM_MARGIN,
        id="normal",
        showBoundary=0,
    )
    doc.addPageTemplates(
        [
            PageTemplate(id="first", frames=[frame], onPage=first_page),
            PageTemplate(id="later", frames=[frame], onPage=later_page),
        ]
    )

    story = [Hero(), Spacer(1, 18)]
    story += [
        SectionCard(
            1,
            PALETTE["red"],
            "No momento do barulho",
            [
                p("<b>Ligue 190</b> toda vez que o barulho acontecer, mesmo que já tenha ligado antes. Cada chamado gera histórico. Quando a viatura chegar, a vítima deve falar com a PM e relatar o fato; isso viabiliza o BOPM no local e fortalece juridicamente o registro."),
                p("Sempre que possível, registre também um <b>Boletim de Ocorrência (BO)</b>:"),
                bullet("Pela Delegacia Eletrônica da Polícia Civil;"),
                bullet("Ou presencialmente em uma Delegacia de Polícia."),
            ],
        ),
        Spacer(1, 12),
        CompactContactsCard(),
        PageBreak(),
        SectionCard(
            2,
            PALETTE["orange"],
            "Essencial: gravem em conjunto com outros vizinhos",
            [
                p("Essa é uma das provas mais importantes. A jurisprudência majoritária entende que a <b>perturbação do sossego (art. 42 da Lei de Contravenções Penais)</b> normalmente exige que o barulho atinja a coletividade ou um número indeterminado de pessoas."),
                p("O ideal é que vários vizinhos:"),
                bullet("Gravem ao mesmo tempo;"),
                bullet("Façam a gravação de dentro de suas residências;"),
                bullet("Mostrem o horário no celular;"),
                bullet("Guardem os vídeos."),
                p("Quanto mais moradores registrarem o mesmo fato, mais robusta será a prova."),
            ],
        ),
        Spacer(1, 12),
        SectionCard(
            3,
            PALETTE["blue"],
            "Procure o NUMEC da Polícia Militar",
            [
                p("Antes de judicializar o caso, tente uma solução por meio da <b>mediação comunitária</b>. Embora o fato tenha ocorrido em Rubiácea, os moradores podem solicitar atendimento junto ao <b>NUMEC (Núcleo de Mediação Comunitária)</b> da 5ª Companhia da Polícia Militar, sediado em Guararapes."),
                p("O NUMEC realiza audiências de mediação entre as partes, buscando uma solução consensual e pacífica para o conflito. A mediação é <b>gratuita, voluntária</b> e costuma resolver muitos conflitos de vizinhança sem necessidade de processo judicial."),
                callout("<b>5ª Companhia da PM:</b> (18) 3606-1347", PALETTE["blue"]),
                p("Procurar por: <b>Cb PM Jurca</b> ou <b>Subten PM Marcos</b>"),
            ],
        ),
        PageBreak(),
        SectionCard(
            4,
            PALETTE["purple"],
            "Comunique também a Prefeitura de Rubiácea",
            [
                p("Além das medidas policiais, o morador pode comunicar o fato à Prefeitura Municipal, permitindo a adoção das providências administrativas cabíveis."),
                p("A <b>Lei Municipal nº 1.602/2014</b> regula ruídos urbanos e protege o bem-estar e o sossego público em Rubiácea. A norma proíbe ruídos, vibrações e sons excessivos ou incômodos que perturbem a coletividade."),
                callout("<b>Prefeitura de Rubiácea:</b> (18) 3697-9117", PALETTE["purple"]),
            ],
        ),
        Spacer(1, 12),
        SectionCard(
            5,
            PALETTE["amber"],
            "Se o problema continuar",
            [
                p("Guarde: protocolos das ligações para o 190, boletins de ocorrência, vídeos, datas e horários das ocorrências."),
                p("Com esse material, é possível enviar uma <b>Notificação Extrajudicial</b> ou procurar o <b>Ministério Público</b> ou o <b>Poder Judiciário</b>, buscando a cessação da perturbação e, quando cabível, indenização por danos morais."),
            ],
        ),
        Spacer(1, 12),
        SectionCard(
            6,
            PALETTE["green"],
            "Por que documentar?",
            [
                p("A documentação organizada fortalece a comprovação dos fatos e aumenta as chances de responsabilização do infrator."),
            ],
        ),
        PageBreak(),
        PlainCard(
            "Base legal",
            [
                bullet("<b>Art. 42 da Lei de Contravenções Penais</b> - Perturbação do trabalho ou do sossego alheios."),
                bullet("<b>Art. 1.277 do Código Civil</b> - Direito ao sossego, à saúde e à segurança nas relações de vizinhança."),
                bullet("<b>Lei Municipal nº 1.602/2014</b> (Ruídos Urbanos de Rubiácea/SP) - Proíbe ruídos, vibrações e sons excessivos ou incômodos que perturbem o sossego e o bem-estar público."),
                bullet("<b>Lei Municipal nº 1.878/2022</b> - Proíbe fogos de estampido e artefatos pirotécnicos de efeito sonoro ruidoso no município."),
            ],
            PALETTE["violet_bg"],
            colors.HexColor("#D9C8FF"),
        ),
        Spacer(1, 12),
        PlainCard(
            "Resumo rápido",
            [
                bullet("<b>Ligue 190</b>"),
                bullet("Faça <b>Boletim de Ocorrência</b>"),
                bullet("Registre o fato com outros vizinhos"),
                bullet("Procure o <b>NUMEC</b> da PM"),
                bullet("Comunique a <b>Prefeitura</b>"),
                bullet("Guarde todas as provas"),
                bullet("Persistindo o problema, busque as medidas judiciais cabíveis"),
            ],
            PALETTE["green_bg"],
            colors.HexColor("#B9E8C4"),
        ),
        Spacer(1, 12),
        PlainCard(
            "Importante",
            [
                p("Vivemos em um Estado Democrático de Direito. Toda restrição de direitos deve observar o devido processo legal, sendo vedadas medidas arbitrárias. A solução dos conflitos deve ocorrer sempre pelos meios legais, com diálogo, mediação e respeito aos direitos de todos."),
            ],
            PALETTE["yellow_bg"],
            colors.HexColor("#FFE4A3"),
        ),
    ]

    doc.build(story)
    print(OUT)


if __name__ == "__main__":
    build()
