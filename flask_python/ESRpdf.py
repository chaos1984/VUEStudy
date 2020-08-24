# -*- coding: utf-8 -*-
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import pandas as pd
import json

# 生成PDF文件
class PDFGenerator:
    def __init__(self, filename):
        self.filename = filename
        # self.file_path = '/xxx/xxx/xxx/xxx/'
        self.title_style = ParagraphStyle(name="TitleStyle",  fontSize=32, alignment=TA_LEFT,leading=32,)
        self.sub_title_style = ParagraphStyle(name="SubTitleStyle", fontSize=32,
                                              textColor=colors.HexColor(0x666666), alignment=TA_LEFT, )
        self.content_style = ParagraphStyle(name="ContentStyle",  fontSize=18, leading=25, spaceAfter=20,
                                            underlineWidth=1, alignment=TA_LEFT, )
        self.foot_style = ParagraphStyle(name="FootStyle", fontSize=14, textColor=colors.HexColor(0xB4B4B4),
                                         leading=25, spaceAfter=20, alignment=TA_CENTER, )
        self.table_title_style = ParagraphStyle(name="TableTitleStyle",  fontSize=20, leading=25,
                                                spaceAfter=10, alignment=TA_LEFT, )
        self.sub_table_style = ParagraphStyle(name="SubTableTitleStyle",  fontSize=16, leading=25,
                                                spaceAfter=10, alignment=TA_LEFT, )
        self.basic_style = TableStyle([('FONTNAME', (0, 0), (-1, -1)),
                                       ('FONTSIZE', (0, 0), (-1, -1), 12),
                                       ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                       ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                       ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                                       # 'SPAN' (列,行)坐标
                                       ('SPAN', (1, 0), (3, 0)),
                                       ('SPAN', (1, 1), (3, 1)),
                                       ('SPAN', (1, 2), (3, 2)),
                                       ('SPAN', (1, 5), (3, 5)),
                                       ('SPAN', (1, 6), (3, 6)),
                                       ('SPAN', (1, 7), (3, 7)),
                                       ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                       ])
        self.common_style = TableStyle([
                                      ('FONTSIZE', (0, 0), (-1, -1), 8),
                                      ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                      ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                      ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                                      ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                     ])

    def genTaskPDF(self, home_data, task_data):
        story = []
        print (home_data)
        print (task_data)
        # 首页内容
        story.append(Spacer(1, 20 * mm))
        # img = Image('/xxx/xxx.png')
        # img.drawHeight = 20 * mm
        # img.drawWidth = 40 * mm
        # img.hAlign = TA_LEFT
        # story.append(img)
        # story.append(Spacer(1, 10 * mm))
        story.append(Paragraph(u"DAB Deployment Simulation Request", self.title_style))
        story.append(Spacer(1, 20 * mm))
        story.append(Paragraph(u"Test Report of XXX", self.sub_title_style))
        story.append(Spacer(1, 45 * mm))
        story.append(Paragraph(u"ESR No.:" + home_data['ESR'], self.content_style))
        story.append(Paragraph(u"PE:" + home_data['PE'], self.content_style))
        story.append(Paragraph(u"Team:" + home_data['Team'], self.content_style))
        story.append(Paragraph(u"Date:" + home_data['Date'], self.content_style))
        story.append(Spacer(1, 55 * mm))
        story.append(Paragraph(u"Autoliv CTC CAE", self.foot_style))
        story.append(PageBreak())

        # 表格允许单元格内容自动换行格式设置
        stylesheet = getSampleStyleSheet()
        body_style = stylesheet["BodyText"]
        body_style.wordWrap = 'CJK'
        body_style.fontName = 'ping'
        body_style.fontSize = 12

        # 测试计划
        story.append(Paragraph(u"Specific Info.", self.table_title_style))
        story.append(Spacer(1, 3 * mm))
        task_table = Table(task_data, colWidths=[25 * mm, 141 * mm], rowHeights=12 * mm, style=self.common_style)
        story.append(task_table)

        story.append(Spacer(1, 10 * mm))


        doc = SimpleDocTemplate(self.filename + ".pdf",
                                leftMargin=20 * mm, rightMargin=20 * mm, topMargin=20 * mm, bottomMargin=20 * mm)


        doc.build(story)
if __name__ == "__main__":
    with open(r"jsonfortest.json", "r") as f:
        home_data = json.loads(f.read())
    a = PDFGenerator('www')
    task_data =data=[("BOM","1" ),("DAB CAD",'A'),("Inflator",'B'),("CushionFile"),("Cases","123")]
    a.genTaskPDF(home_data, task_data)