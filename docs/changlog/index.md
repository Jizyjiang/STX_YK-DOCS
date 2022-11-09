# 日志：
**11月7日：**
1. 将大屏幕led的亮度降低到95 原值：128
2. 当直播时，直播视频文件将会存储到D盘中的live-vidoes文件夹中。
3. 将ProPresenter降级到7.9.2版本
4. 重新开放了ProPresenter的网络控制功能，
   在Companion中 ProPresenter控制可用：上一张，下一张，全清，清楚幻灯 清除背景，可以使用了。
5. 冻结了ProPresenter的数据库，直到教程编写完成。
**注意：**
**1.如果大家需要添加什么长久文档，可以发给我，我审核后会添加进去。
  2.特别需要注意的是，不要随意重启系统，系统重启后，ProPresenter将会恢复到冻结时的状态。也就是说你需要重新准备今日的幻灯文稿**


* Handle wifi connection to access point, fallback to provide own WiFi network in case no connection could be made.
* Vue.js based Webinterface for configuration
* Hosts unaltered electrodacus HTML file (apart from data URL)
* Provides raw data as read by HTML file (you can still use any local HTML file, just change the data URL to `http://[the IP of the device]/rawData`)
* Receiving and caching data from SBMS with unaltered firmware. (ignores AT commands)
* Parsing data from SBMS, usable by Consumers like the MQTT client. (currently only live data)
* MQTT client: publish live data in JSON format whenever it is received from the SBMS main board
* OTA Updates via ArduinoOTA