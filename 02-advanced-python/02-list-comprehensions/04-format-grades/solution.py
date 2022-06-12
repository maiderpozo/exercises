def format_grades(grades):
    def avg(ns):
        return round(sum(ns) / len(ns))

    return "\n".join( f'{name}: {avg(grades)}' for name, grades in grades.items() )

print(format_grades({ 'John': [17, 11, 8], 'Ann': [13, 10, 10], 'Robert': [13, 15, 9, 14] }))