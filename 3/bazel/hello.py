from absl import app
from absl import flags
from typing import List

FLAGS = flags.FLAGS
flags.DEFINE_string("name", None, "Your name.")
flags.DEFINE_integer("num_times", 1,
                     "Number of times to print greeting.")

# Required flag.
flags.mark_flag_as_required("name")

def main(argv):
  del argv  # Unused.
  hollers = Salutations(FLAGS.num_times, FLAGS.name)

  for holla in hollers:
    print(holla)

def Salutations(count: int, name: str) -> List[str]:
    output = list()
    for i in range(0, count):
        print('Hello, %s' % name)
    return output

if __name__ == '__main__':
  app.run(main)