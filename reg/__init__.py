import winreg


class REG:
    _keypath = ''

    def __init__(self, root=r'SOFTWARE\WWD\PPAY'):
        if root > '':
            self._keypath = root
        return

    def _keyexists(self):
        exists = False
        try:
            reg = winreg.CreateKey(winreg.HKEY_CURRENT_USER, self._keypath)
            batchno = winreg.QueryValue(reg, 'batchno')
            winreg.CloseKey(reg)
            exists = True
        except:
            pass
        return exists

    def _create_batchno(self, batchno):
        reg = winreg.CreateKey(winreg.HKEY_CURRENT_USER, self._keypath)
        winreg.SetValue(reg, 'batchno', winreg.REG_SZ, batchno)
        winreg.CloseKey(reg)
        return

    def _get_batchno(self):
        batchno = ''
        try:
            reg = winreg.CreateKey(winreg.HKEY_CURRENT_USER, self._keypath)
            batchno = winreg.QueryValue(reg, 'batchno')
            winreg.CloseKey(reg)
            exists = True
        except:
            pass
        return batchno

    def get_batch_no(self):
        batch_no = ''
        if self._keyexists():
            batch_no = self._get_batchno()
        else:
            self._create_batchno(batch_no)
        return batch_no

    def save_batch_no(self, batch_no):
        try:
            reg = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, self._keypath)
            winreg.SetValue(reg, 'batchno',winreg.REG_SZ, batch_no)
            winreg.CloseKey(reg)
        except:
            pass
        return

    def save_str(self, key, value):
        try:
            reg = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, self._keypath)
            winreg.SetValue(reg, key,winreg.REG_SZ, value)
            winreg.CloseKey(reg)
        except:
            pass
        return

    def load_str(self, key):
        value = ''
        try:
            reg = winreg.CreateKey(winreg.HKEY_CURRENT_USER, self._keypath)
            value = winreg.QueryValue(reg, key)
            winreg.CloseKey(reg)
            exists = True
        except:
            pass
        return value
