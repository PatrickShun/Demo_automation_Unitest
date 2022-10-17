import unittest
import logging
import uiautomator2 as u2
from time import sleep



# 初始化：python -m uiautomator2 init


class TestPorsche(unittest.TestCase):
    def setUp(self):
        self.idevice = u2.connect()
        self.idevice.implicitly_wait(10)
        self.logger = logging.getLogger()
        self.logger.setLevel('DEBUG')
        self.fmt = logging.Formatter('%(filename)s-%(lineno)d-%(asctime)s-%(levelname)s-%(message)s')
        self.file_handler = logging.FileHandler('mylog.log')
        self.file_handler.setLevel('DEBUG')
        self.file_handler.setFormatter(self.fmt)
        self.logger.addHandler(self.file_handler)
        self.idevice.screenshot('001.png')

    def test_init(self):
        Current_APP_Activity = self.idevice.app_current()['activity']
        if Current_APP_Activity == 'com.ticauto.weather.WeatherContainerActivity':
            self.logger.debug('test_init_Current_APP_Activity:%s' % Current_APP_Activity)
        else:
            self.idevice.app_start(package_name='com.ticauto.weather',
                                   activity='com.ticauto.weather.WeatherContainerActivity', wait=True)
            self.logger.debug('assertEqual error, reopen com.ticauto.weather:id/weather_layout')

    def test_WeatherTitle(self):
        try:
            Current_APP_Activity = self.idevice.app_current()['activity']
            self.assertEqual(Current_APP_Activity, 'com.ticauto.weather.WeatherContainerActivity')
            title_Text = self.idevice.xpath('//*[@resource-id="com.ticauto.weather:id/title"]').get_text()
            self.assertEqual('Weather', title_Text)
            self.logger.debug('test_WeatherTitle:%s' % title_Text)
        except:
            print('test_WeatherTitle_error')

    def test_city_name(self):
        cityName = self.idevice.xpath('//*[@resource-id="com.ticauto.weather:id/city_name"]').get_text()
        self.assertEqual('普洱市江城哈尼族彝族自治县', cityName)
        self.logger.debug('current city name is : %s' % cityName)

    def test_add_city(self):
        addCityName = '花都区'
        self.idevice.xpath('//*[@resource-id="com.ticauto.weather:id/city_name"]').click()
        self.idevice.xpath('//*[@resource-id="com.ticauto.weather:id/add_city"]').click()
        self.idevice.xpath('//*[@resource-id="com.ticauto.weather:id/search_text"]').set_text(addCityName)
        sleep(1)
        self.idevice.xpath('//*[@resource-id="com.ticauto.weather:id/city_list"]/android.widget.LinearLayout[1]').click()
        self.idevice.press('home')
        sleep(2)
        self.idevice.app_start(package_name='com.ticauto.weather', activity='com.ticauto.weather.WeatherContainerActivity', wait=True)
        sleep(2)
        pageIndex = len(self.idevice(className='android.widget.RadioButton'))
        for m in range(pageIndex-1):
            self.idevice.swipe(1170, 370, 250, 370, 0.2)
            sleep(2)






if __name__ == '__main__':
    unittest.main()
