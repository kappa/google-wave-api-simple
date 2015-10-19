"""Kappabot robot."""
# vim: set fileencoding=utf-8 :

__author__ = 'kapranoff@gmail.com (Alex Kapranoff)'

from waveapi import events
from waveapi import model
from waveapi import robot

def OnParticipantsChanged(properties, context):
  """Invoked when any participants have been added/removed."""
  added = properties['participantsAdded']
  for p in added:
    if p == 'k-appa@appspot.com':
      Setup(context)
      break


def Setup(context):
  """Called when this robot is first added to the wave."""
  root_wavelet = context.GetRootWavelet()
  root_wavelet.CreateBlip().GetDocument().SetText("I'm alive (2)!")


def OnBlipCreated(properties, context):
  """Invoked when a new blip is created in the wave."""
  blip_id = properties['blipId']
  blip = context.GetBlipById(blip_id).GetDocument().AppendText("(kappa here)");


if __name__ == '__main__':
  kapbot = robot.Robot('K-appa the Kappabot',
		  image_url='http://kapranoff.ru/~kappa/motoicon.jpg',
                      profile_url='http://k-appa.appspot.com/')
  kapbot.RegisterHandler(events.WAVELET_PARTICIPANTS_CHANGED,
                        OnParticipantsChanged)
  kapbot.RegisterHandler(events.WAVELET_BLIP_CREATED,
                        OnBlipCreated)
  kapbot.Run()
