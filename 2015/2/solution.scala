// class Package(val length: Int, val width: Int, val height: Int):
  
//   def sides(): Array[Int] = Array(length * width, width * height, length * height)

//   def surfaceArea(): Int = 2 * sides().sum

//   def materialArea(): Int = surfaceArea() + sides().min

def wrappingPaperArea(line: String): Int =
  val Array(length, width, height) = line.split("x").map(_.toInt)

  val sides = Array(length * width, width * height, length * height)

  2 * sides.sum + sides.min

def ribbonLength(line: String): Int =
  val Array(length, width, height) = line.split("x").map(_.toInt)

  val perimeters = Array(
    2 * length + 2 * width,
    2 * width + 2 * height,
    2 * length + 2 * height,
  )

  val volume = length * width * height

  perimeters.min + volume


@main def main =
  val source = scala.io.Source.fromFile("input.txt")
  val lines = source.getLines.toArray

  println(lines.map(wrappingPaperArea).sum)

  println(lines.map(ribbonLength).sum)

  source.close()