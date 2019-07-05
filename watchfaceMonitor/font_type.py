import os

def get_font_type(font_type):
    fontType = font_type.split('_')
    font = '_'.join(fontType[1:-1])
    fontsize = int(fontType[-1])
    fontPath = os.path.join(os.getcwd(), 'fonts')
    fontFile = get_font_file(font, fontPath)
    return fontFile, fontsize


def get_font_file(font, fontPath):
    fontDict = {
    'DINCONDENSED_BOLD': 'DINCondensed-Bold.ttf',
    'DINNEXTFORHUAWEI_BOLD': 'DINNextForHuawei-Bold.ttf',
    'DIN_BLACKITALIC': 'DIN-BlackItalic.otf',
    'DIN_BLACKALTERNATE': 'DIN-BlackAlternate.otf',
    'DINNEXTLTPRO_MEDIUM': 'DINNextLTPro-Medium.otf',
    'DINNEXTLTPRO_REGULAR': 'DINNextLTPro-Regular.otf',
    'EUROSTILELT_DEMI': 'EurostileLT-Demi.ttf',
    'EUROSTILELT_BOLD_EXTENDED2': 'EurostileLT-Bold-Extended2.ttf',
    'HYQIHEI_60S': 'HYQiHei-60S.ttf',
    'ROBOTOCONDENSED_REGULAR': 'RobotoCondensed-Regular.ttf',
}
    fontFile = os.path.join(fontPath, fontDict[font])
    return fontFile


if __name__ == "__main__":
    fontList = [
    'F_DINCONDENSED_BOLD_38',
    'F_DINCONDENSED_BOLD_42',
    'F_DINCONDENSED_BOLD_44',
    'F_DINCONDENSED_BOLD_50',
    'F_DINCONDENSED_BOLD_60',
    'F_DINCONDENSED_BOLD_70',
    'F_DINCONDENSED_BOLD_82',
    'F_DINCONDENSED_BOLD_90',
    'F_DINCONDENSED_BOLD_106',
    'F_DINCONDENSED_BOLD_116',
    'F_DINNEXTFORHUAWEI_BOLD_16',
    'F_DINNEXTFORHUAWEI_BOLD_22',
    'F_DINNEXTFORHUAWEI_BOLD_24',
    'F_DINNEXTFORHUAWEI_BOLD_28',
    'F_DINNEXTFORHUAWEI_BOLD_40',
    'F_DINNEXTFORHUAWEI_BOLD_80',
    'F_DIN_BLACKITALIC_32',
    'F_DIN_BLACKITALIC_84',
    'F_DIN_BLACKALTERNATE_52',
    'F_DINNEXTLTPRO_MEDIUM_32',
    'F_DINNEXTLTPRO_REGULAR_24',
    'F_DINNEXTLTPRO_REGULAR_46',
    'F_EUROSTILELT_DEMI_14',
    'F_EUROSTILELT_DEMI_20',
    'F_EUROSTILELT_DEMI_32',
    'F_EUROSTILELT_DEMI_34',
    'F_EUROSTILELT_BOLD_EXTENDED2_42',
    'F_HYQIHEI_60S_20',
    'F_HYQIHEI_60S_23',
    'F_HYQIHEI_60S_26',
    'F_HYQIHEI_60S_28',
    'F_HYQIHEI_60S_30',
    'F_HYQIHEI_60S_38',
    'F_HYQIHEI_60S_48',
    'F_ROBOTOCONDENSED_REGULAR_20',
    'F_ROBOTOCONDENSED_REGULAR_23',
    'F_ROBOTOCONDENSED_REGULAR_26',
    'F_ROBOTOCONDENSED_REGULAR_28',
    'F_ROBOTOCONDENSED_REGULAR_30',
    'F_ROBOTOCONDENSED_REGULAR_38',
    'F_ROBOTOCONDENSED_REGULAR_48'
    ]
    for font_type in fontList:
        get_font_type(font_type)   