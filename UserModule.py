

class User:

    def getUsereStimate(self, arr):
        userData = {}
        studStimate = 0

        for i in range(len(arr)):
            for j in range(len(arr[i][1])):
                studName = arr[i][0]
                userGrup = arr[i][2]
                imgLink = arr[i][3]
                Link = arr[i][4]
                studStimate += arr[i][1][j]

            userData.update({i: {
                "username": studName,
                "userGrup": userGrup,
                'imgLink': imgLink,
                'link': Link,
                'Stimate': studStimate / 4
            }})

            studStimate = 0

        return userData

    def payments(self, money, stud, coff=[0, 0.75, 1, 1.35]):

        student = self.getUsereStimate(stud)
        money = int(money)
        bank = (money / len(student))
        cof2 = float(coff[0])
        cof3 = float(coff[1])
        cof4 = float(coff[2])
        cof5 = float(coff[3])

        for i in range(len(student)):
            if student[i].get("Stimate") <= 2.0:
                student[i].update({"payments": bank*cof2})
                continue

            if student[i].get("Stimate") <= 3.0:
                student[i].update({"payments": bank*cof3})
                continue

            if student[i].get("Stimate") <= 4.0:
                student[i].update({"payments": bank*cof4})
                continue

            if student[i].get("Stimate") <= 5.0:
                student[i].update({"payments": bank*cof5})
                continue

        return student
