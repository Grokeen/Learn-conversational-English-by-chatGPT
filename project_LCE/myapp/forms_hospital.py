# 다양한 사용자 입력에 대한 양식
from django import forms
from .models_hospital import ActionsLog, Image, AnalysisResult


# 202405110138 김용록 각 모델 폼 작성
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file_path', 'uploaded_timestamp', 'source']
        
class AnalysisResultForm(forms.ModelForm):
    class Meta:
        model = AnalysisResult
        fields = ['image', 'detected_text', 'detected_objects','analysis_timestamp']  
        
class ActionsLogForm(forms.ModelForm):
    class Meta:
        model = ActionsLog
        fields = ['result', 'action_description', 'action_timestamp']
        