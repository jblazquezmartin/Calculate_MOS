import math

latency = 160 # miliseconds
jitter = 50 # miliseconds
packet_loss = 2 # percentage
codec_delay = 10.0

def calculate_mos(jitter, packet_loss, latency, codec_delay):
    effective_latency = latency + jitter*2 + codec_delay
    if effective_latency < 160:
        r = 93.2 - (effective_latency / 40)
    else:
        r = 93.2 -((effective_latency - 120) / 10)

    r -= 2.5 * packet_loss
    if r < 0:
        mos = 1.0
    else:
        mos = 1 + 0.035*r + 0.000007*r*(r-60)*(100-r)

    print("R factor: ", r)
    

    return mos

mos = calculate_mos(jitter, packet_loss, latency, codec_delay)
print("mos: ", mos)
