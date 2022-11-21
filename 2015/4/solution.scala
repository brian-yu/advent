import java.security.MessageDigest

def findAnswer(secretKey: String, n: Int): Option[Int] =
  var num = 0

  while (true)
    val hash = (
      MessageDigest.getInstance("MD5").digest(s"$secretKey$num".getBytes)
      .map("%02X".format(_)).mkString
    )

    if (hash.slice(0, n) == "0" * n)
      return Some(num)

    num += 1
  
  None

@main def main =
  val secretKey = "bgvyzdsv"
  
  println(findAnswer(secretKey, 5))
  println(findAnswer(secretKey, 6))

  