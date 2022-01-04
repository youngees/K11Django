from django import forms
from django.forms.widgets import PasswordInput 
'''
장고에서 제공하는 Form기능을 사용하려면 우선 forms.Form 클래스를 상속한다.
각 변수명은 해당 input태그의 name속성값으로 사용된다. 
태그 생성시 required 속성이 포함되어 기본적인 빈값 검증을 하게된다. 
'''

class QuestionForm(forms.Form):
    # <input type=text>를 생성. label은 타이틀로 사용
    user_id = forms.CharField(label='아이디', max_length=10)
    # 가장 기본적인 input태그를 생성. 타이틀은 title로 표시됨
    title = forms.CharField()
    # 여러줄의 텍스트를 입력할 수 있는 <textarea>를 생성.
    content = forms.CharField(widget=forms.Textarea)
    # 기본적인 input태그를 생성하되 type='email'로 생성.
    email = forms.EmailField()
    # <input type = checkbox>를 생성. 유효성 검증을 하지 않는다.
    my_check = forms.BooleanField(required=False)


class QuestionForm2(forms.Form):
    user_id = forms.CharField(label='작성자', max_length=10)
    passwd = forms.CharField(label='패스워드', widget=PasswordInput)
    title = forms.CharField(label='제목')
    content = forms.CharField(label='내용', widget=forms.Textarea)
    file = forms.FileField(label='첨부파일', required=False)

    