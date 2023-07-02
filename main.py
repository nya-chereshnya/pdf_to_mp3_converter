import pdfplumber
from pathlib import Path
from gtts import gTTS


class PDFParser:
    def __init__(self) -> None:
        self.PDF_EXTENSION: str = '.pdf'

    def _validate_path(self, file_path) -> bool:
        if Path(file_path).is_file() and Path(file_path).suffix == self.PDF_EXTENSION:
            print('File exists!')
            return True
        print('File not exists, check the file path!')
        return False

    def input_file_path(self) -> str:
        while True:
            file_path: str = str(input('Input .pdf file path: '))
            if self._validate_path(file_path):
                return file_path

    def _remove_line_breaks(self, text: str) -> str:
        return text.replace('\n', ' ')

    def convert_pdf_to_text(self, pdf_file_path: str) -> str:
        with pdfplumber.open(pdf_file_path) as pdf:
            converted_text = ''.join([page.extract_text()
                                     for page in pdf.pages])
            return self._remove_line_breaks(converted_text)


class MP3Generator:
    def __init__(self) -> None:
        self.ENGLISH: str = 'en'
        self.RUSSIAN: str = 'ru'

    def _validate_language(self, lang: str) -> bool:
        if lang == self.ENGLISH or lang == self.RUSSIAN:
            return True
        return False

    def _set_mp3_languege(self) -> str:
        while True:
            lang = str(input('Set mp3 language (en or ru): '))
            if self._validate_language(lang):
                return lang
            print('Incorrect!')

    def _validate_path(self, file_path: str) -> bool:
        if Path(file_path).is_dir():
            return True
        return False

    def set_file_path(self) -> str:
        while True:
            save_path: str = str(input('Set .mp3 file save path: '))
            if self._validate_path(save_path):
                return save_path
            print('Incorrect path!')

    def convert_text_to_mp3(self, audiofile_name: str, text: str, path_to_save: str) -> None:
        lang = self._set_mp3_languege()
        my_audio = gTTS(text=text, lang=lang)
        print('Converting text to mp3...')
        my_audio.save(f'{path_to_save}\\{audiofile_name}.mp3')
        print('Done!')


if __name__ == '__main__':
    pdf_parser = PDFParser()
    pdf_file_path = pdf_parser.input_file_path()
    text_from_pdf_file = pdf_parser.convert_pdf_to_text(pdf_file_path)
    mp3_generator = MP3Generator()
    mp3_path = mp3_generator.set_file_path()
    auidiofile_name = Path(pdf_file_path).stem
    mp3_generator.convert_text_to_mp3(
        auidiofile_name, text_from_pdf_file, mp3_path)
