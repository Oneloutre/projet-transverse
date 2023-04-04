def returnDisplayFormMatrixLine(content, form, line):
    display = ''
    for number in content[form][line]:
        if number == 1:
            display += "■" + " "
        else:
            display += "  "
    return display


def returnDisplayGridMatrixLine(content, line):
    display = ''
    for number in content[line]:
        if number == 1:
            display += " ."
        elif number == 0:
            display += "  "
        else:
            display += ' ' + "■"
    return display
