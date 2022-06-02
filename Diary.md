# 雑記

initがコンストラクタの役割をもつことについては理解したが、引数にselfが入っている意味が???である
ないとどうなるんだろう
~~あと、もしかしたら違うかもしれないがメソッドの使い方がJavaと違うような気がする。~~

~~Javaだと(Sample.)foo.bar()は(Sample"クラス"に入っている)foo"フィールド"のbar"関数"を呼ぶことを表すが~~  
~~Pythonだとfoo.bar()はfoo"インスタンス"のbar"関数"を呼ぶことを表す~~  
~~と認識してる（いい例が思い浮かばなかった...）~~
どっちも書き方自体同じだった。  
違いはインスタンス化された実体の元のクラス中のメソッドを呼ぶと、foo.bar()（foo"インスタンス"、bar"メソッド"）となる。インスタンス化せずにあるクラスのメソッドを直接呼んだ場合には、Sample.foo.bar()（Sample"クラス"、foo"フィールド"、bar"メソッド"）となる。  

~~DynamoDBについてSDKを用いたCreateTableの仕方は偶然分かったが、create_tableメソッド中のself引数の意味がよくわからなかった。~~  
解決した。PythonのSyntax Sugar記法にしなかったことによるものだった。
今回の例でいうと、
`create_table(self, table_name)`  
ではselfとtable_nameを引数としており、通常の書き方であるSyntax Sugar記法ではselfは書かないためKintoreクラスからインスタンス化したdynamodbインスタンスを用いて、  
`dynamodb.create_table('TrainingRecord')`  
と書ける。ところが、その記法を用いないと以下のようにも書ける（同値）  
`Kintore.create_table(dynamodb,'TrainingRecord')`  
シンプルに不思議だった。  
> http://blog.livedoor.jp/odaxsen/archives/1653675.html

JavaやPython、Cはそれぞれ関数へ引数として変数を指定する際の変数の扱いがそれぞれ異なり、Javaは参照値渡し、Pythonは参照渡し、Cは値渡しらしい。Cのポインタ渡しが参照渡しと同じ。

> BOOL、L、M、N、NS、S、SS などのデータ型記述子は、JSON データ形式でのデータ型に対応します。  
> https://docs.aws.amazon.com/ja_jp/sdk-for-net/v3/developer-guide/dynamodb-expressions.html

らしい。また、

> The following is a complete list of DynamoDB data type descriptors:  
> S – String  
> N – Number  
> B – Binary  
> BOOL – Boolean  
> NULL – Null  
> M – Map  
> L – List  
> SS – String Set  
> NS – Number Set  
> BS – Binary Set  
> https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.LowLevelAPI.html

らしい。

今回はDayにはN、WhereにはSを使おうと思う。Dayはyyyymmdd形式、Whereは部位（Chest、Legなど）を想定しているため。
add_tableはうまく使えてないため明日以降検証