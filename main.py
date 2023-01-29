import io
import sys
sys.stdout = io.StringIO()
sys.stderr = io.StringIO()
from UserModule import User
import eel


def start():
    eel.init('www', allowed_extensions=['.html', '.css', '.favicon'])
    eel.start('index.html')


@eel.expose
def addBlock(money, cof):
    stud = [
        ["Ляхов А.А.", [2, 2, 2, 2], '221-323',
            'https://www.timeoutdubai.com/cloud/timeoutdubai/2021/09/11/udHvbKwV-IMG-Dubai-UAE-1.jpg', 'link-to-profile'],
        ["Ляхов А.А.", [3, 3, 3, 3], '221-323',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRm81XoZa9dFFAFPY-LjxgJ-XAj-KeySicSvw&usqp=CAU', 'link-to-profile'],
        ["Ляхов А.А.", [4, 4, 4, 4], '221-323',
            'http://www.imgworlds.com/wp-content/uploads/2015/11/1-PLANYOURVISIT-ticketbookings420X290.jpg', 'link-to-profile'],
        ["Ляхов А.А.", [5, 5, 5, 5], '221-323',
            'http://www.imgworlds.com/wp-content/uploads/2015/11/cf-thumb.jpg', 'link-to-profile'],
        ["Ляхов А.А.", [5, 5, 5, 5], '221-323',
            'http://www.imgworlds.com/wp-content/uploads/2015/11/1-PLANYOURVISIT-PARKRULES420X290.jpg', 'link-to-profile'],
        ["Ляхов А.А.", [5, 5, 5, 5], '221-323',
            'https://i.ytimg.com/vi/fJohAXpQUZw/maxresdefault.jpg', 'link-to-profile'],
        ["Ляхов А.А.", [5, 5, 5, 5], '221-323',
            'https://delamazonas.com/wp-content/uploads/2020/11/800px-Un_mono_ardilla_posa_sobre_la_cabeza_de_una_turista-LOW.jpg', 'link-to-profile'],
        ["Ляхов А.А.", [5, 5, 5, 5], '221-323',
            'https://delamazonas.com/wp-content/uploads/2020/11/800px-Un_mono_ardilla_posa_sobre_la_cabeza_de_una_turista-LOW.jpg', 'link-to-profile'],
        ["Ляхов А.А.", [5, 5, 5, 5], '221-323',
            'https://delamazonas.com/wp-content/uploads/2020/11/800px-Un_mono_ardilla_posa_sobre_la_cabeza_de_una_turista-LOW.jpg', 'link-to-profile'],
        ["Ляхов А.А.", [5, 5, 5, 5], '221-323',
            'https://delamazonas.com/wp-content/uploads/2020/11/800px-Un_mono_ardilla_posa_sobre_la_cabeza_de_una_turista-LOW.jpg', 'link-to-profile'],
        ["Ляхов А.А.", [5, 5, 5, 5], '221-323',
            'https://delamazonas.com/wp-content/uploads/2020/11/800px-Un_mono_ardilla_posa_sobre_la_cabeza_de_una_turista-LOW.jpg', 'link-to-profile'],
        ["Ляхов А.А.", [5, 5, 5, 5], '221-323',
            'https://delamazonas.com/wp-content/uploads/2020/11/800px-Un_mono_ardilla_posa_sobre_la_cabeza_de_una_turista-LOW.jpg', 'link-to-profile'],
        ["Ляхов А.А.", [5, 5, 5, 5], '221-323',
            'https://delamazonas.com/wp-content/uploads/2020/11/800px-Un_mono_ardilla_posa_sobre_la_cabeza_de_una_turista-LOW.jpg', 'link-to-profile'],
        ["Ляхов А.А.", [5, 5, 5, 5], '221-323',
            'https://delamazonas.com/wp-content/uploads/2020/11/800px-Un_mono_ardilla_posa_sobre_la_cabeza_de_una_turista-LOW.jpg', 'link-to-profile'],
    ]

    student = [User().payments(money, stud, cof)]

    return student


if __name__ == "__main__":
    eel.browsers.set_path("chrome", "./src/chrome-win/chrome.exe")
    start()
