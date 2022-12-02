import os
import json
from time import sleep
from kafka import KafkaProducer

if __name__ == '__main__':
    producer = KafkaProducer(
        bootstrap_servers=[
            'b-1.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092'
        ],
        # Encode all values as JSON
        # value_serializer=lambda value: json.dumps(value).encode(),
    )

    transaction: dict = {'headline': 'በመተከል ዞን የማንቡክ ከተማ ነዋሪዎች የፀጥታ ኃይል አባላት ሰንጋዎችን አበረከቱ', 'category': 'ሀገር አቀፍ ዜና', 'article': 'መተከል (ኢዜአ) በቤኒሻንጉል ጉሙዝ ክልል መተከል ዞን የማንቡክ ከተማ ነዋሪዎች በዞኑ ሕግ በማስከበር ሥራ ላይ ለሚገኘው የፀጥታ ሃይል አባላት ለገና በዓል 210 ሺህ ብር ወጪ የተደረገባቸው ስድስት የእርድ ሠንጋዎችን አበረከቱ።በፌዴራል መንግሥት የተቋቋመው ግብረ ሃይል በመተከል ዞን ፀረ ሰላም ሃይሎችን በማደንና በአካባቢው ዘላቂ ሰላምና መረጋጋት ለመፍጠር እየሠራ ይገኛል።ግብረ ሃይሉ ከዞን\nእስከ ቀበሌ ባለው\nመዋቅር በተንኮልና ሴራ\nውስጥ የገቡ አመራሮችን\nየማጥራት፣ ህዝባዊ አንድነትን\nየማጠናከርና ኢኮኖሚያዊና ማህበራዊ\nችግሮችን የመፍታት ሥራዎችን\nአጠናክሮ ቀጥሏል።\xa0በአካባቢው በዜጎች ላይ ጥቃት በመፈፀም በተለያዩ አካባቢዎች የሚንቀሳቀሱ ሽፍቶችን በማደን ለሕግ የማቅረብ ሥራም በማከናወን ላይ ነው።ግብረ ሃይሉ ባከናወነው ተግባር በርካታ አካባቢዎች ወደ ቀደመ ሰላማቸው እየተመለሱ ሲሆን ህዝባዊ የውይይት መድረኮችም በመካሄድ ላይ ናቸው።በዚህም ደስተኞች ነን ሲሉ አስተያየታቸውን የሰጡ በዞኑ ዳንጉር ወረዳ የማንቡክ ከተማ ነዋሪዎች ተናግረዋል።ነዋሪዎቹ ለፀጥታ ሃይሉ ያላቸውን ድጋፍ ለማሳየት የበዓል መዋያውን ማበርከታቸውን ገልፀዋል።ግብረ ሃይሉ በአካባቢው ስላመጣው አንፃራዊ ሰላም ደስተኞች መሆናቸውን የገለፁት ነዋሪዎቹ፤ ድጋፋቸው እንደሚቀጥል አረጋግጠዋል።በዳንጉር ወረዳ ህዝቡ ባደረገው ውይይት ህዝብን ከህዝብ የማጋጨትና ማንነትን መሰረት ያደረገ ጥቃት እንዲፈፀም ያደረጉ አካላት ተለይተው እርምጃ እንዲወሰድባቸው ጠይቀዋል።የአካባቢው ማህበረሰብ ማንኛውንም በዓል በጋራ የማክበርና የአብሮነት ልምድ እንዳለው የገለፁት የአካባቢቅው ሽማግሌዎች\n“የገና በዓልን በለመድነው አብሮነት እያከበርን ነው” ብለዋል።ማህበረሰቡ የለገሰውን ስጦታ\nየተረከቡት ሻለቃ ፍቃዱ\nጃፍራ ለተደረገው ድጋፍ\nሁሉ በሠራዊቱ ስም\nአመስግነዋል።አዲስ ዘመን ታህሳስ 30/2013'}
    message: str = json.dumps(transaction)
    producer.send("g2-topics-test", value=message.encode()).get(timeout=30)

    print("PRODUCED")

    # while True:
    #     transaction: dict = create_random_transaction()
    #     producer.send(TRANSACTIONS_TOPIC, value=transaction)
    #     print(transaction)  # DEBUG
    #     sleep(SLEEP_TIME)