import cmd, sys, os
import numpy as np
import audio_utils as au

# allowed audio extensions
EXTENSIONS = ['.mp3', '.wav', '.MP3', '.WAV']

def is_audio_file(filepath):

	if os.path.exists(filepath):
		if any([filepath.endswith(e) for e in EXTENSIONS]):
			return True
		
	
		
	return False

class Main(cmd.Cmd):
	intro = ''
	prompt = '#'

	def __init__(self):
		super().__init__()
		self.mode = None
		self.output_path = None

	def do_load_file(self, path):
		'Carica un file singolo'

		print("Carico %s..." % (path))
		if is_audio_file(path):
			self.cur_filename = path.split('/')[-1]
			self.cur_data, self.cur_sr = au.load(path)
			self.mode = 'single'
			print("File caricato")
		else:
			print("Errore: specificare un file valido")

	def do_load_dir(self, path):
		'Pre-carica una cartella da processare in batch'
		if not os.path.isdir(path):
			print("Cartella non trovata")
			return
		file_list = os.listdir(path)
		# filter by extension
		self.input_path = path
		self.file_list = [f for f in file_list if is_audio_file(os.path.join(path, f))]
		N = len(self.file_list)
		print("Trovati %d file" % (N))
		self.mode = 'batch'

	def do_save(self, arg):
		'Salva il file caricato nella cartella specificata'
		if self.output_path is None:
			print("Errore: specificare un percorso di salvataggio valido con il comando set_output")
			return
		if self.mode == 'single':
			print("Salvo %s..." % (self.cur_filename))
			filepath = os.path.join(path, self.cur_filename)
			au.write(filepath, self.cur_sr, self.cur_data)
		else:
			print("Non disponibile in modalità batch")

	def do_set_output(self, path):
		'Imposta la cartella di output per il salvataggio'
		print("Percorso di output: "+path)
		if not os.path.isdir(path):
			os.makedirs(path)
		self.output_path = path

	def do_trim_silence(self, arg):
		'Rimuove il silenzio iniziale'
		print("TODO")

	def do_quit(self, arg):
		'Esce dal programma'
		print("Ciao")
		#self.close()
		sys.exit()

if __name__ == '__main__':
	Main().cmdloop()