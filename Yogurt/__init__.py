__version__ = '1.0'
__author__ = "Philip Herron"
__email__ = "redbrain@gcc.gnu.org"
__url__ = "https://github.com/redbrain"

def testingResetCache():
    AppCache.CacheServer = None
    AppCache.CacheServer = AppCache.CacheSystem({'type': 'local'})
    return AppCache.CacheServer
