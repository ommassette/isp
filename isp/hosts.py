from django_hosts import host, patterns

host_patterns = patterns('',
    # Main website
    host(r'isp-qq06', 'isp.urls', name='www'),
    # Admin subdomain
    host(r'admin\.isp-qq06', 'isp.admin_urls', name='admin'),
)