import util
import os


def determine_codec(text, tmp_fname='tmp.txt'):
    with open('allcodecs.txt', 'r') as f:
        codecs = f.read().split()
    
    good_codecs = set()
    for codec in codecs:
        try:
            ctext = text.encode().decode(codec)
            print(ctext)
            #with open(tmp_fname, 'w') as f:
            #    f.write(ctext)
                
            good_codecs.add(codec)
        except UnicodeDecodeError:
            pass
        except UnicodeEncodeError:
            pass
    if os.path.exists(tmp_fname):
        os.remove(tmp_fname)
    return good_codecs
            

        
        
if __name__ == '__main__':

    limit = None
    
    # get user, pair, and chat data
    fname = '../data/all_firebase_data.pickle'
    users, pairs, chats = util.get_filtered_data(fname)
    print(f'{len(users)} users, {len(pairs)} pairs, {len(chats)} chats.')
    
    msgs = '.'.join([c['message'] for c in chats])
    print(determine_codec(msgs))
    
    #print(chats['LzljVxFZvVXR20SK1cXm'][0].keys())
    
    #df = pd.DataFrame(chats)

    #print(df.head())
    
    
    
    


        
        
        