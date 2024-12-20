import urllib.request
import zipfile
import glob
import shutil
import os
import re

unique_class_ids = set()

def replace_class_local_identifier(in_contents, class_id, enum_name):
  return in_contents.replace(enum_name, '__EasyAirwindows_' + class_id + '_' + enum_name)

def process_file(in_name, in_ext, in_contents):
  class_id = in_name
  if class_id[-4:] == 'Proc':
    class_id = class_id[:-4]
  unique_class_ids.add(class_id)

  includes_str = '#include <EasyAirwindows/EasyAirwindowsAudioEffectX.h>\n'
  if in_ext == '.cpp':
    includes_str += '#include <EasyAirwindows/' + class_id + '.h>\n'

  out_base_contents = '''\
/* ========================================
 *  This file was generated by: https://github.com/iffyloop/EasyAirwindows
 *  Based on Airwindows source: https://github.com/airwindows/airwindows
 *  Please refer to Airwindows author information contained later in this file
 * ======================================== */

#pragma once

''' + includes_str + '''\

#pragma warning(push)
#pragma warning(disable : 4996)

namespace EasyAirwindows {

'''

  out_contents = in_contents
  out_contents = re.sub(r'#include.*', '', out_contents)
  out_contents = re.sub(r'#ifndef.*', '', out_contents)
  out_contents = re.sub(r'#define.*', '', out_contents)
  out_contents = re.sub(r'#endif.*', '', out_contents)
  out_contents = re.sub(r'AudioEffect\s*\*\s*createEffectInstance.*?\}', '', out_contents, flags=re.DOTALL)
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kParam')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kNumParameters')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kNumPrograms')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kNumInputs')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kNumOutputs')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kUniqueId')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kDKAD')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kDKCD')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kPEAK')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kSLEW')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kSUBS')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kMONO')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kSIDE')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kVINYL')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kAURAT')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kMONORAT')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kMONOLAT')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kPHONE')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kCANSA')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kCANSB')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kCANSC')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kCANSD')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kTRICK')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'primeL')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'primeR')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kshortA')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kshortB')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kshortC')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kshortD')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kshortE')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kshortF')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kshortG')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kshortH')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kshortI')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kshortJ')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kshortK')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kshortL')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kshortM')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kshortN')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kshortO')
  out_contents = replace_class_local_identifier(out_contents, class_id, 'kshortP')
  out_contents = out_contents.replace('M_PI', '__EasyAirwindows_M_PI')
  out_contents = out_contents.replace('kVstMaxProgNameLen', '__EasyAirwindows_kVstMaxProgNameLen')
  out_contents = out_contents.replace('kVstMaxParamStrLen', '__EasyAirwindows_kVstMaxParamStrLen')
  out_contents = out_contents.replace('kVstMaxProductStrLen', '__EasyAirwindows_kVstMaxProductStrLen')
  out_contents = out_contents.replace('kVstMaxVendorStrLen', '__EasyAirwindows_kVstMaxVendorStrLen')
  out_contents = out_contents.replace('kPlugCategEffect', '__EasyAirwindows_kPlugCategEffect')
  out_contents = out_contents.replace('AudioEffect', 'EasyAirwindowsAudioEffect')
  out_contents = out_contents.replace('audioMasterCallback', '__EasyAirwindows_audioMasterCallback')
  out_contents = out_contents.replace('VstPlugCategory', '__EasyAirwindows_VstPlugCategory')
  out_contents = out_contents.replace('VstInt32', '__EasyAirwindows_VstInt32')
  out_contents = out_contents.replace('vst_strncpy', '__EasyAirwindows_vst_strncpy')
  out_contents = out_contents.replace('float2string', '__EasyAirwindows_float2string')
  out_contents = out_contents.replace('dB2string', '__EasyAirwindows_dB2string')
  out_contents = out_contents.replace('int2string', '__EasyAirwindows_int2string')
  out_contents = out_contents.replace('audioeffectx.h', 'EasyAirwindowsAudioEffectX.h')
  out_contents = out_base_contents + out_contents + '\n}\n\n#pragma warning(pop)\n'

  return out_contents

def generate_index_file():
  unique_class_ids_list = list(unique_class_ids)
  unique_class_ids_list.sort()

  includes_str = '#include <EasyAirwindows/EasyAirwindowsIndex.h>\n'
  for class_id in unique_class_ids_list:
    includes_str += '#include <EasyAirwindows/' + class_id + '.h>\n'

  out_contents = '''\
/* ========================================
 *  This file was generated by: https://github.com/iffyloop/EasyAirwindows
 * ======================================== */

#pragma once

''' + includes_str + '''\

namespace EasyAirwindows {

namespace Index {

static const char * const __EasyAirwindowsEffectNames[] = {
'''

  for class_id in unique_class_ids_list:
    out_contents += '  "' + class_id + '",\n'

  out_contents += '''\
};

const int NUM_EFFECT_IDS = ''' + str(len(unique_class_ids)) + ''';

const char * const getEffectName(int effectId) {
  if (effectId < NUM_EFFECT_IDS) {
    return __EasyAirwindowsEffectNames[effectId];
  } else {
    return nullptr;
  }
}

EasyAirwindowsAudioEffectX *createEffect(int effectId) {
  switch (effectId) {
'''

  for i in range(len(unique_class_ids_list)):
    out_contents += '  case ' + str(i) + ':\n    return new ' + unique_class_ids_list[i] + '(nullptr);\n'

  out_contents += '''\
  default:
    return nullptr;
  }
}

void destroyEffect(EasyAirwindowsAudioEffectX *effect) {
  delete effect;
}

}

}
'''

  return out_contents

def delete_sources():
  print('Deleting original Airwindows sources')
  try:
    os.remove('airwindows-master.zip')
  except FileNotFoundError:
    pass
  try:
    shutil.rmtree('airwindows-master')
  except FileNotFoundError:
    pass

def delete_outputs():
  print('Deleting stale output')
  try:
    shutil.rmtree('out')
  except FileNotFoundError:
    pass

def main():
  delete_sources()
  delete_outputs()

  print('Downloading Airwindows repository from GitHub')
  urllib.request.urlretrieve('https://github.com/airwindows/airwindows/archive/refs/heads/master.zip', 'airwindows-master.zip')

  print('Extracting Airwindows repository')
  with zipfile.ZipFile('airwindows-master.zip', 'r') as zipf:
    zipf.extractall('.')

  print('Setting up')

  os.mkdir('out')
  os.mkdir('out/EasyAirwindows')

  for glob_filename in glob.glob('airwindows-master/plugins/MacVST/*/source/*.cpp') + glob.glob('airwindows-master/plugins/MacVST/*/source/*.h'):
    print('Processing ' + glob_filename)
    basename = os.path.basename(glob_filename)
    basename_no_ext, basename_ext = os.path.splitext(basename)
    out_path = os.path.join('out/EasyAirwindows', basename)
    with open(glob_filename, 'r') as inf:
      with open(out_path, 'w') as outf:
        outf.write(process_file(basename_no_ext, basename_ext, inf.read()))

  print('Copying base files')
  shutil.copyfile('EasyAirwindowsAudioEffectX.h', 'out/EasyAirwindows/EasyAirwindowsAudioEffectX.h')
  shutil.copyfile('EasyAirwindowsIndex.h', 'out/EasyAirwindows/EasyAirwindowsIndex.h')

  print('Generating index file')
  with open('out/EasyAirwindows/EasyAirwindowsIndex.cpp', 'w') as outf:
    outf.write(generate_index_file())

  delete_sources()

if __name__ == '__main__':
  main()
