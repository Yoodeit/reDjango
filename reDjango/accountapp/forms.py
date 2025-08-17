from django.contrib.auth.forms import UserCreationForm


class accountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        # 초기화 이후에 딱 username 필드만 변경해주는겁니다.
        self.fields['username'].disabled = True