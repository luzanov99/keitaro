from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class DateFilterForm(forms.Form):
    FILTER_CHOICES =(
    ("today", "Сегодня"),
    ("all_time", "За все время"),
    ("yesterday", "Вчера"),
    ("diapazon", "Диапазон дат"),
    ("1_month_ago", "Один месяц назад"),
)
    data_name = forms.ChoiceField(choices=FILTER_CHOICES,widget=forms.Select(attrs={'onchange': 'showDiv("id_start_date_month", this);showDiv("id_start_date_day", this);showDiv("id_start_date_year", this);showDiv("id_end_date_day", this);showDiv("id_end_date_month", this);showDiv("id_end_date_year", this);'}),required=False)
    start_date = forms.DateField(input_formats='%Y,%m,%d',widget=forms.SelectDateWidget(years=range(2015, 2025)), required=False)
    end_date = forms.DateField(input_formats='%Y,%m,%d',widget=forms.SelectDateWidget(years=range(2015, 2025)), required=False)