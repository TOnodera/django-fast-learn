from django import forms


class BookForm(forms.Form):

    isbn = forms.CharField(
        label="ISBNコード",
        required=True,
        max_length=20,
        error_messages={
            "required": "ISBNは必須です。",
            "max_length": "２０文字以内で入力して下さい。"
        })
    title = forms.CharField(
        label="書名",
        required=True,
        max_length=100,
        error_messages={
            "required": "書名は必須です。",
            "max_length": "１００文字以内で入力して下さい。"
        })
    price = forms.IntegerField(
        label="価格",
        required=True,
        min_value=100,
        error_messages={
            "required": "価格は必須です。",
            "max_length": "整数で入力して下さい。"
        })
    publisher = forms.ChoiceField(label="出版社", choices=[
        ('翔泳社', '翔泳社'),
        ('技術評論社', '技術評論社'),
        ('秀和システム', '秀和システム'),
        ('SBクリエイティブ', 'SBクリエイティブ'),
        ('日経BP', '日経BP')
    ])
    published = forms.DateField(
        label='刊行日',
        required=True,
        error_messages={
            "required": "刊行日は必須です。",
            "invalid": "刊行日はYYYY-MM-DDの形式で入力して下さい。"
        })
