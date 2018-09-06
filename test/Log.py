

class Log:
    def __init__(self):
        self.alpr = open('AlprLog.txt', 'w+')
        self.mult = 0

    def alpr_print(self, num, mult, results, finish):
        # self.alpr.write("FRAME " + str(num+mult) + '\n' + str(results['plate']) + '\n\n')
        self.alpr.write("FRAME " + str(num + mult) + '\n')
        i = 1
        for plate in results:
            self.alpr.write('Plate ' + str(i) + ' ' + plate['plate'] + ' Confidence ' + str(plate['confidence']) + ' Coordinates ' + str(plate['coordinates']) + '\n')
            i += 1
        self.alpr.write('Time Taken: ' + str(finish) + '\n')
        self.alpr.write('\n')

    def alpr_close(self):
        self.alpr.close()

    def add_mult(self, num):
        self.mult = self.mult + num
