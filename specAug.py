import numpy as np

def applyAugment(mel, aug_type, mask_numb):
    '''
    input
        - mel : (max_mel_len, n_mels)
    '''

    if aug_type == 0:
        # apply mask certain freq component
        v = np.shape(mel)[-1]
        Fp = 27

        for _ in range(mask_numb):
            f = np.random.choice(Fp)
            f0 = np.random.choice(v-f) 
            mel[:, f0:f0+f] = 0

    else:
        # apply mask certain time component
        tau = len(mel)
        T = 20 # max mask len
        for _ in range(mask_numb):
            t = np.random.choice(T)
            t0 = np.random.choice(tau-t)
            mel[t0:t0+t, :] = 0

    return mel