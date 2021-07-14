import React, {useCallback, useState, useEffect } from 'react';
import { Alert, Button, Image, View, Platform, Text } from 'react-native';
import * as ImagePicker from 'expo-image-picker';

export default function ImagePickerExample() {

    const [image, setImage] = useState(null);
    const [caption, setCap] = useState(null);

    const pickImage = useCallback(async () => {
        try {
            const { granted } = await ImagePicker.requestCameraPermissionsAsync();
            console.log('granted', granted)
            if (!granted) {
                Alert.alert('Error', 'Sorry, we need camera roll permissions to make this work!');
                return
            }
    
            var result = await ImagePicker.launchCameraAsync({
                allowsEditing: false,
                aspect: [4, 3],
                quality: 1,
            });
    
            if (!result.cancelled) {
                setImage(result.uri);
            
                let localUri = result.uri;
                // Infer the type of the image

                const uploadData = new FormData();
                uploadData.append('title', 'image');
        
                if (Platform.os !== 'web') {
                    uploadData.append('cover', { name: 'cover.jpg', type: 'image/jpg', uri: localUri });
                } else {
                    uploadData.append('cover', localUri, 'cover.png');                
                }
                const res = await fetch('http://f2a835d85dc2.ngrok.io/books/', {
                    method: 'POST',
                    body: uploadData,
                    headers: {
                        'Content-Type': 'multipart/form-data; ',
                    },
                })
                const data = await res.json() //  res.text();
                console.log('res:', data)
            }
        } catch (e) {
            console.log('eee', e)
        }

        const res = await fetch('http://f2a835d85dc2.ngrok.io/get_caption/', {
                        method: 'GET',
                    })
        const data = await res.json() //  res.text();
        console.log('res:', data)
        setCap(data.caption)

        }, []);
    
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>  
       
      <Button title="Pick an image from camera roll" onPress={pickImage} />
      {image && <Image source={{ uri: image }} style={{ width: 350, height: 350 }} />}
      
      
      {caption && <Text>{caption} </Text> }

    </View>
  );
};