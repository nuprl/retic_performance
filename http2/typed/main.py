from retic import Void
from iri2uri import Iri2Uri
from Timer import Timer
import os


#bg
def main()->Void:
    iri2uri = Iri2Uri().iri2uri
    ### 1. test correctness on invariant iri
    invariant = [
        "ftp://ftp.is.co.za/rfc/rfc1808.txt",
        "http://www.ietf.org/rfc/rfc2396.txt",
        "ldap://[2001:db8::7]/c=GB?objectClass?one",
        "mailto:John.Doe@example.com",
        "news:comp.infosystems.www.servers.unix",
        "tel:+1-816-555-1212",
        "telnet://192.0.2.16:80/",
        "urn:oasis:names:specification:docbook:dtd:xml:4.1.2" ]
    for uri in invariant:
        if not (uri == iri2uri(uri)):
            raise AssertionError("test 1")
    ### 2. test correctness on variant iri
    if not("http://xn--o3h.com/%E2%98%84" == iri2uri("http://\N{COMET}.com/\N{COMET}")):
        raise AssertionError("test 2")
    if not("http://bitworking.org/?fred=%E2%98%84" == iri2uri("http://bitworking.org/?fred=\N{COMET}")):
        raise AssertionError("test 3")
    if not("http://bitworking.org/#%E2%98%84" == iri2uri("http://bitworking.org/#\N{COMET}")):
        raise AssertionError("test 4")
    if not("#%E2%98%84" == iri2uri("#\N{COMET}")):
        raise AssertionError("test 5")
    if not("/fred?bar=%E2%98%9A#%E2%98%84" == iri2uri("/fred?bar=\N{BLACK LEFT POINTING INDEX}#\N{COMET}")):
        raise AssertionError("test 6")
    if not("/fred?bar=%E2%98%9A#%E2%98%84" == iri2uri(iri2uri("/fred?bar=\N{BLACK LEFT POINTING INDEX}#\N{COMET}"))):
        raise AssertionError("test 7")
    #assertNotEqual("/fred?bar=%E2%98%9A#%E2%98%84", iri2uri("/fred?bar=\N{BLACK LEFT POINTING INDEX}#\N{COMET}".encode('utf-8')))
    ### 3. stress test
    iri2uri = Iri2Uri().iri2uri
    testfile = os.path.join(os.path.dirname(__file__), "sample_urls.csv")
    with open(testfile) as fd:
        for ln in fd:
            url = ln.split(",", 1)[0]
            iri2uri(url)
    return

t = Timer()
with t:
    for i in range(10):
        main()
