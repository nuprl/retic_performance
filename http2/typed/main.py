from retic import Void
from iri2uri import Iri2Uri
from benchmark_tools.Timer import Timer
import os


def assertEqual(s1:String, s2:String)->Void:
    if s1 == s2:
        return
    else:
        raise AssertionError("'%s' is not equal to '%s'" % (s1, s2))

def assertNotEqual(s1:String, s2:String)->Void:
    if s1 == s2:
        raise AssertionError("'%s' is equal to '%s'" % (s1, s2))
    else:
        return

def test_uris()->Void:
    """Test that URIs are invariant under the transformation."""
    iri2uri = Iri2Uri().iri2uri
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
        assertEqual(uri, iri2uri(uri))

def test_iri():
    """ Test that the right type of escaping is done for each part of the URI."""
    iri2uri = Iri2Uri().iri2uri
    assertEqual("http://xn--o3h.com/%E2%98%84", iri2uri("http://\N{COMET}.com/\N{COMET}"))
    assertEqual("http://bitworking.org/?fred=%E2%98%84", iri2uri("http://bitworking.org/?fred=\N{COMET}"))
    assertEqual("http://bitworking.org/#%E2%98%84", iri2uri("http://bitworking.org/#\N{COMET}"))
    assertEqual("#%E2%98%84", iri2uri("#\N{COMET}"))
    assertEqual("/fred?bar=%E2%98%9A#%E2%98%84", iri2uri("/fred?bar=\N{BLACK LEFT POINTING INDEX}#\N{COMET}"))
    assertEqual("/fred?bar=%E2%98%9A#%E2%98%84", iri2uri(iri2uri("/fred?bar=\N{BLACK LEFT POINTING INDEX}#\N{COMET}")))
    #assertNotEqual("/fred?bar=%E2%98%9A#%E2%98%84", iri2uri("/fred?bar=\N{BLACK LEFT POINTING INDEX}#\N{COMET}".encode('utf-8')))

#bg
def test_correctness()->Void:
    test_uris()
    test_iri()

#bg
def test_stress()->Void:
    iri2uri = Iri2Uri().iri2uri
    testfile = os.path.join(os.path.dirname(__file__), "sample_urls.csv")
    with open(testfile) as fd:
        for ln in fd:
            url = ln.split(",", 1)[0]
            iri2uri(url)
    return

#bg
def main()->Void:
    test_correctness()
    test_stress()
    return

t = Timer()
with t:
    for i in range(10):
        main()
