# -*- mode: python -*-

block_cipher = None

a = Analysis(['main.py'],
             pathex=['.'],
             binaries=[],
             datas=[
                 ('./data/python.ico', './win10toast/data'),
                 ('./data/VERSION', './scrapy'),
                 ('./data/mime.types', './scrapy')
             ],
             hiddenimports=[
                 'scrapy.cmdline', 'scrapy.command', 'scrapy.commands.bench', 'scrapy.commands.check',
                 'scrapy.commands.crawl', 'scrapy.commands.edit', 'scrapy.commands.fetch', 'scrapy.commands.genspider',
                 'scrapy.commands.list', 'scrapy.commands.parse', 'scrapy.commands.runspider',
                 'scrapy.commands.settings', 'scrapy.commands.shell', 'scrapy.commands.startproject',
                 'scrapy.commands.version', 'scrapy.commands.view', 'scrapy.conf', 'scrapy.contracts.default',
                 'scrapy.contrib.closespider', 'scrapy.contrib.corestats', 'scrapy.contrib.debug',
                 'scrapy.contrib.downloadermiddleware.ajaxcrawl', 'scrapy.contrib.downloadermiddleware.chunked',
                 'scrapy.contrib.downloadermiddleware.cookies', 'scrapy.contrib.downloadermiddleware.decompression',
                 'scrapy.contrib.downloadermiddleware.defaultheaders',
                 'scrapy.contrib.downloadermiddleware.downloadtimeout', 'scrapy.contrib.downloadermiddleware.httpauth',
                 'scrapy.contrib.downloadermiddleware.httpcache', 'scrapy.contrib.downloadermiddleware.httpcompression',
                 'scrapy.contrib.downloadermiddleware.httpproxy', 'scrapy.contrib.downloadermiddleware.redirect',
                 'scrapy.contrib.downloadermiddleware.retry', 'scrapy.contrib.downloadermiddleware.robotstxt',
                 'scrapy.contrib.downloadermiddleware.stats', 'scrapy.contrib.downloadermiddleware.useragent',
                 'scrapy.contrib.feedexport', 'scrapy.contrib.httpcache', 'scrapy.contrib.linkextractors.htmlparser',
                 'scrapy.contrib.linkextractors.lxmlhtml', 'scrapy.contrib.linkextractors.regex',
                 'scrapy.contrib.linkextractors.sgml', 'scrapy.contrib.loader.common',
                 'scrapy.contrib.loader.processor', 'scrapy.contrib.logstats', 'scrapy.contrib.memdebug',
                 'scrapy.contrib.memusage', 'scrapy.contrib.pipeline.files', 'scrapy.contrib.pipeline.images',
                 'scrapy.contrib.pipeline.media', 'scrapy.contrib.spidermiddleware.depth',
                 'scrapy.contrib.spidermiddleware.httperror', 'scrapy.contrib.spidermiddleware.offsite',
                 'scrapy.contrib.spidermiddleware.referer', 'scrapy.contrib.spidermiddleware.urllength',
                 'scrapy.contrib.spiders.crawl', 'scrapy.contrib.spiders.feed', 'scrapy.contrib.spiders.init',
                 'scrapy.contrib.spiders.sitemap', 'scrapy.contrib.spiderstate', 'scrapy.contrib.statsmailer',
                 'scrapy.contrib.throttle', 'scrapy.contrib_exp.downloadermiddleware.decompression',
                 'scrapy.contrib_exp.iterators', 'scrapy.core.downloader.contextfactory',
                 'scrapy.core.downloader.handlers.datauri', 'scrapy.core.downloader.handlers.file',
                 'scrapy.core.downloader.handlers.ftp', 'scrapy.core.downloader.handlers.http',
                 'scrapy.core.downloader.handlers.http10', 'scrapy.core.downloader.handlers.http11',
                 'scrapy.core.downloader.handlers.s3', 'scrapy.core.downloader.middleware',
                 'scrapy.core.downloader.tls', 'scrapy.core.downloader.webclient', 'scrapy.core.engine',
                 'scrapy.core.scheduler', 'scrapy.core.scraper', 'scrapy.core.spidermw', 'scrapy.crawler',
                 'scrapy.downloadermiddlewares.ajaxcrawl', 'scrapy.downloadermiddlewares.chunked',
                 'scrapy.downloadermiddlewares.cookies', 'scrapy.downloadermiddlewares.decompression',
                 'scrapy.downloadermiddlewares.defaultheaders', 'scrapy.downloadermiddlewares.downloadtimeout',
                 'scrapy.downloadermiddlewares.httpauth', 'scrapy.downloadermiddlewares.httpcache',
                 'scrapy.downloadermiddlewares.httpcompression', 'scrapy.downloadermiddlewares.httpproxy',
                 'scrapy.downloadermiddlewares.redirect', 'scrapy.downloadermiddlewares.retry',
                 'scrapy.downloadermiddlewares.robotstxt', 'scrapy.downloadermiddlewares.stats',
                 'scrapy.downloadermiddlewares.useragent', 'scrapy.dupefilter', 'scrapy.dupefilters',
                 'scrapy.exceptions', 'scrapy.exporters', 'scrapy.extension', 'scrapy.extensions.closespider',
                 'scrapy.extensions.corestats', 'scrapy.extensions.debug', 'scrapy.extensions.feedexport',
                 'scrapy.extensions.httpcache', 'scrapy.extensions.logstats', 'scrapy.extensions.memdebug',
                 'scrapy.extensions.memusage', 'scrapy.extensions.spiderstate', 'scrapy.extensions.statsmailer',
                 'scrapy.extensions.telnet', 'scrapy.extensions.throttle', 'scrapy.http.common', 'scrapy.http.cookies',
                 'scrapy.http.headers', 'scrapy.http.request.form', 'scrapy.http.request.rpc',
                 'scrapy.http.response.html', 'scrapy.http.response.text', 'scrapy.http.response.xml',
                 'scrapy.interfaces', 'scrapy.item', 'scrapy.link', 'scrapy.linkextractor',
                 'scrapy.linkextractors.htmlparser', 'scrapy.linkextractors.lxmlhtml', 'scrapy.linkextractors.regex',
                 'scrapy.linkextractors.sgml', 'scrapy.loader.common', 'scrapy.loader.processors', 'scrapy.log',
                 'scrapy.logformatter', 'scrapy.mail', 'scrapy.middleware', 'scrapy.pipelines.files',
                 'scrapy.pipelines.images', 'scrapy.pipelines.media', 'scrapy.project', 'scrapy.resolver',
                 'scrapy.responsetypes', 'scrapy.selector.csstranslator', 'scrapy.selector.lxmlsel',
                 'scrapy.selector.unified', 'scrapy.settings.default_settings', 'scrapy.settings.deprecated',
                 'scrapy.shell', 'scrapy.signalmanager', 'scrapy.signals', 'scrapy.spider', 'scrapy.spiderloader',
                 'scrapy.spidermanager', 'scrapy.spidermiddlewares.depth', 'scrapy.spidermiddlewares.httperror',
                 'scrapy.spidermiddlewares.offsite', 'scrapy.spidermiddlewares.referer',
                 'scrapy.spidermiddlewares.urllength', 'scrapy.spiders.crawl', 'scrapy.spiders.feed',
                 'scrapy.spiders.init', 'scrapy.spiders.sitemap', 'scrapy.squeue', 'scrapy.squeues', 'scrapy.stats',
                 'scrapy.statscol', 'scrapy.statscollectors', 'scrapy.telnet', 'scrapy.tmp', 'scrapy.utils.benchserver',
                 'scrapy.utils.boto', 'scrapy.utils.conf', 'scrapy.utils.console', 'scrapy.utils.datatypes',
                 'scrapy.utils.decorator', 'scrapy.utils.decorators', 'scrapy.utils.defer', 'scrapy.utils.deprecate',
                 'scrapy.utils.display', 'scrapy.utils.engine', 'scrapy.utils.ftp', 'scrapy.utils.gz',
                 'scrapy.utils.http', 'scrapy.utils.httpobj', 'scrapy.utils.iterators', 'scrapy.utils.job',
                 'scrapy.utils.log', 'scrapy.utils.markup', 'scrapy.utils.misc', 'scrapy.utils.multipart',
                 'scrapy.utils.ossignal', 'scrapy.utils.project', 'scrapy.utils.python', 'scrapy.utils.reactor',
                 'scrapy.utils.reqser', 'scrapy.utils.request', 'scrapy.utils.response', 'scrapy.utils.serialize',
                 'scrapy.utils.signal', 'scrapy.utils.sitemap', 'scrapy.utils.spider', 'scrapy.utils.template',
                 'scrapy.utils.test', 'scrapy.utils.testproc', 'scrapy.utils.testsite', 'scrapy.utils.trackref',
                 'scrapy.utils.url', 'scrapy.xlib.pydispatch', 'scrapy.xlib.tx', 'scrapy._monkeypatches'
             ],
             hookspath=['.'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=True)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main')
