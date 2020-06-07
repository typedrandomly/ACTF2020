import gmpy2
from Cryptodome.Util.number import *
a=2417338317401331712061117407518523422879235109995422964912592140637402316491894788332348297809531063771699269056939336427134502419061270721512979591311
N=8873711467349818367463967026951546601575294305617194253400575802375444177851800308693658804190737539724076127184801814678401300235323478526898845330590215100166025350276223829414953871052570134783455100298295010912439792347381517311589197605934558485064897417257250428564837452287599709107676052894822139931
c=755942670161748393598641531301385779868128781550590222599612601576353032825250190293112023973608391031945463967735414074353191097973716054662816937744145336720772362339423163116416709815713319105290692961646765676644563440597855070881293314880297072438472924155996283287641772039893365082938460907545614679
e=65537
for k in range(2**19,2**21):
    #print(gmpy2.iroot(k*k+4*N, 2)[0])
    q = (-a + gmpy2.iroot(a*a+4*k*N, 2)[0])//(2*k)
    p = k*q+a
    #print(k)
    if(p*q==N):
        #print (k)
        phi = (p-1)*(q-1)
        d = gmpy2.invert(e,phi)
        m = pow(c,d,N)
        print (long_to_bytes(m))
        break