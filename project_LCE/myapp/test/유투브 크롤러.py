'''
pip install pytube3
'''

from pytube import YouTube


#url에 있는 유튜브의 정보들 저장
video_url = 'https://www.youtube.com/watch?v=Zg3j6anDU6U' 
yt = YouTube(video_url)


#영상 기본 정보 가져오기
print("[영상 제목]", yt.title)  # 영상제목
print("[영상 게시자]", yt.author) # 영상 게시자
print("[조회수]", yt.views)
print("[평균평점]", yt.rating) # 평균 평점
print("[영상길이(초)]", yt.length)
print("[연령제한여부]", yt.age_restricted)
print("[영상 설명]", yt.description) # 영상 설명
print("[썸네일URL]", yt.thumbnail_url) # 썸네일 url 주소


#영상 리스트 확인
yt.streams.all()


#다운받을 영상 선택하기
# 전송 포맷 중 첫번째 선택
stream = yt.streams.all()[0]
stream   # <Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">


'''
# 내가 원하는 영상만 선택하기
# 음성만 선택시
yt.streams.filter(only_audio = True).all()
'''
# 내가 원하는 영상만 선택하기
# mp4만 선택시
yt.streams.filter(file_extension = 'mp4').all( )


# 영상 다운로드
stream.download()



# 파일 이름 지정 
## 폴더지정 가능
stream.download(output_path='test', filename = 'KOBE', filename_prefix= 'R.I.P_')




