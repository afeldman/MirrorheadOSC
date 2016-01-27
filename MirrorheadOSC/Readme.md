# MirrorheadOSC

## Generals 
MirrorheadOSC uses the open sound controll protocol to send the Mirrorhead projector controller server commands.
I put the commands into a class structure to support easy access to the commands.

## Usage
This library uses **python3**`not **python2** and **pythonosc 1.5** library. To use lib include the module into your *PYTHONPATH*
environment variable. 
 
```python
ìmport MirrorheadOSC as mhosc

projector = mhosc()
projector.fullscreen()
```

## License
**The project supports the MIT Licence.**