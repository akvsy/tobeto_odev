PYTEST DECORATORS
**@pytest.mark.parametrize:** Bu dekoratörü kullanarak, aynı test fonksiyonunu farklı parametrelerle birden fazla kez çağırabilir.  Test fonksiyonu bu parametrelerle otomatik olarak çağrılır ve her bir çağrı için bir ayrı test oluşturulur.

**@pytest.fixture:** Bu dekoratör ile bir fixture fonksiyonu tanımlanır. Bu fonksiyon, daha sonra fonksiyonlarda kullanılacak veritabanı bağlantısını oluşturur. Başka bir fonksiyonda veritabanı bağlantısına erişmek için pytest.fixture ile oluşturduğumuz fonksiyon ismini yeni oluşturduğumuz fonksiyonumuzun parametre kısmına ekleriz. Test fonksiyonumuz çalıştığında fixture fonksiyonu otomatik olarak çağrılır ve bu fixture fonksiyonunun dönüş değeri test fonksiyonuna geçirilir.

**@pytest.mark.skip:** Bir test fonksiyonunu atlamak için kullanılır. Test koşullarının sağlanmadığı durumlarda bir testi geçici olarak atlamak için kullanılabilir.

 **@pytest.mark.skipif :** Belirli bir koşulun doğru olduğu durumlarda testin geçici olarak atlanmasını sağlar. Koşul, parantez içinde bir Python ifadesi olarak verilir.
**@pytest.mark.xfail:** Bir testin beklediğimiz bir şekilde başarısız olmasını belirtmek için kullanılır.  Testin başarısız olmasının bir sorun olmadığı durumlar için kullanılır.
