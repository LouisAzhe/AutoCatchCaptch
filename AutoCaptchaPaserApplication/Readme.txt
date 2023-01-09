● Driver Path ：
C:/Users/[UserName]/Downloads/AutoCaptcha/chromedriver.exe

● Web Site URL
地政：
https://ep.land.nat.gov.tw/Content/ValidateNumber.ashx?0.4552969179373152
家事：
https://domestic.judicial.gov.tw/judbp/wkw/WHD9HN01/VERIFY_CODE_IMAGE.htm

● Image Xpath(地政、家事)：
/html/body/img

● Save Folder Name：
儲存資料夾名稱(會自動生成，確保資料夾中沒有重名，建議英文命名)

● Crawler Number：
要擷取多少張圖片(建議每次1000~2000以內比較不會被網站檔)

● Time Wait Catch：
每張擷取間隔多少秒以上(建議最小設定0.5)

● 例外：(備註)稅務目前無法使用本軟體擷取
稅務：
https://www.etax.nat.gov.tw/etwmain/login/ic?cert_type=2
● Xpath(稅務) 可再修改程式：
//*[@id="etwMainContent"]/div[2]/div/div[2]/jhi-main/login-ic/div/div/form/div[2]/div/div[2]/etw-captcha/div/img