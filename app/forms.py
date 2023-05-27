from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, TextAreaField, FileField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class ReviewForm(FlaskForm):
    name = StringField("Имя", validators=[
        DataRequired(message='Поле "Имя" не может быть пустым'),
        Length(max=255, message="Имя не может быть длинее 255 символов")
    ])
    review = TextAreaField("Отзыв", validators=[
        DataRequired(message='Поле "Отзыв" не может быть пустым')
    ])
    rating = SelectField("Рейтинг", choices=range(1, 11))
    submit = SubmitField("Отправить отзыв")


class MovieForm(FlaskForm):
    title = StringField("Название фильма", validators=[
        DataRequired(message='Поле "Название фильма" не может быть пустым'),
        Length(max=255, message="Название фильма не может быть длинее 255 символов")
    ])
    description = TextAreaField("Описание", validators=[
        DataRequired(message='Поле "Описание" не может быть пустым')
    ])
    image = FileField("Постер", validators=[
        FileRequired(message="Нельзя добавить фильм без постера")
    ])
    submit = SubmitField("Добавить фильм")
