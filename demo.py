import uiautomator2 as u2

d = u2.connect()
# nn = d.xpath('//*[@resource-id="com.ticauto.weather:id/radios"]/android.widget.RadioButton').count()
lxs = d(className='android.widget.RadioButton')
lxs = len(lxs)
print(lxs)