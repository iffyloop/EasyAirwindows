# EasyAirwindows

The EasyAirwindows script wraps the popular Airwindows audio effect collection for easy integration with any C++ project, just like an external library, instead of exporting the effects as VST/AU formats.

## Setup

```sh
git clone https://github.com/iffyloop/EasyAirwindows.git
cd EasyAirwindows
python3 main.py
```

The `out` directory now contains a folder called `EasyAirwindows` which you may add to your include path.

## Usage

```cpp
#include <EasyAirwindows/EasyAirwindowsIndex.h>

// List the names of all available Airwindows effects
for (int i = 0; i < EasyAirwindows::Index::NUM_EFFECT_IDS; ++i) {
  std::cout << EasyAirwindows::Index::getEffectName(i) << std::endl;
}

// Create an effect
auto effect = EasyAirwindows::Index::createEffect(0); // Pass the ID of the desired effect as an argument

// Destroy an effect
EasyAirwindows::Index::destroyEffect(effect);
```

## License

Your choice of Public Domain (Unlicense) or MIT No Attribution - please read the [LICENSE](LICENSE) file for more details. This license applies only to the `main.py` script, `EasyAirwindowsIndex.h`, and `EasyAirwindowsIndex.cpp`. `EasyAirwindowsAudioEffectX.h` is based on [airwin2clap](https://github.com/baconpaul/airwin2clap/blob/main/LICENSE.md) and is MIT-licensed. All generated files are based on [Airwindows](https://github.com/airwindows/airwindows/blob/master/LICENSE) which is MIT-licensed.
