import cmd, sys, os
import librosa
import essentia
import numpy as np

# allowed audio extensions
EXTENSIONS = ['.mp3', '.wav']

class Main(cmd.Cmd):
	intro = ''
	prompt = '#'
	self.file_list = []

	def do_load_file(self, path):
		'Carica un file singolo'

	def do_load_dir(self, path):
		'Carica una cartella da processare in batch'
		file_list = os.listdir(path)
		# filter by extension
		self.input_path = path
		self.file_list = [f for f in file_list if any([f.endswith(e.lower()) for e in EXTENSIONS])]
		N = len(self.file_list)
		print("Trovati %d file" % (N))

	def do_save(self, path):
		'Salva il/i file elaborati nella cartella specificata'
		if not os.path.isdir(path):
			print("Errore: specificare un percorso di salvataggio valido")
			return
		for f in self.file_list:
			f_path = os.path.join(path, f)

	def do_trim_silence(self, arg):
		'Rimuove il silenzio iniziale'

	def do_quit(self, arg):
		'Esce dal programma'
		print("Ciao")
		#self.close()
		sys.exit()

if __name__ == '__main__':
	Main().cmdloop()