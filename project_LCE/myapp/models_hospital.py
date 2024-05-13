from django.db import models



class Image(models.Model):
    file_path = models.CharField(max_length=255)
    uploaded_timestamp = models.DateTimeField()
    source = models.CharField(max_length=100)

    def __str__(self):
        return self.file_path

class AnalysisResult(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='analysis_results')
    detected_text = models.TextField()
    detected_objects = models.TextField()
    analysis_timestamp = models.DateTimeField()

    def __str__(self):
        return f"Analysis for Image ID {self.image.id}"

class ActionsLog(models.Model):
    result = models.ForeignKey(AnalysisResult, on_delete=models.CASCADE, related_name='actions_logs')
    action_description = models.TextField()
    action_timestamp = models.DateTimeField()

    def __str__(self):
        return f"Action Log ID {self.id} for Result ID {self.result.id}"