def grades(name):
    with open('grades.txt', 'r') as f_in:
        text = f_in.readlines()
        name = name.strip()
        name = name.title()
        for line in text:
            if name in line:
                a = line.split()
                for i in a:
                    if i == '2':
                        print('Извините, но у вас есть двойки, вы отчислены :(')
                        exit()
        for line in text:
            if name in line:
                k = line.split()
                for i in k:
                    if i != '2':
                        print('Вы всё сдали, молодцы :)')
                        exit()


def main():
    grades(input())