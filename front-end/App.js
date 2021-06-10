import React, { useState, useEffect } from 'react';
import { Button, Image, View, Platform, TextInput  } from 'react-native';
import * as ImagePicker from 'expo-image-picker';

export default function ImagePickerExample() {
//////////////////////////////////
    // const [ title, setTitle ] = useState("");
    // const [ cover, setCever ] = useState();
    // //const [text, onChangeText] = React.useState("Useless Text");

    // const newBook = () => {
    //     const uploadData = new FormData();
    //     uploadData.append('title', title);
    //     uploadData.append('cover', cover);
    //     console.log('cover', cover);
    //     fetch('http://127.0.0.1:8000/books/', {
    //     method: 'POST',
    //     body: uploadData
    //     })
    //     .then( res => console.log('res:', res))
    //     .catch(error => console.log(error))
        
    // }
//////////////////////////////////////
    const [image, setImage] = useState(null);

    useEffect(() => {
        (async () => {
        if (Platform.OS !== 'web') {
            const { status } = await ImagePicker.requestMediaLibraryPermissionsAsync();
            if (status !== 'granted') {
            alert('Sorry, we need camera roll permissions to make this work!');
            }
        }
        })();
    }, []);

    const pickImage = async () => {
        var result = await ImagePicker.launchImageLibraryAsync({
        mediaTypes: ImagePicker.MediaTypeOptions.All,
        allowsEditing: true,
        aspect: [4, 3],
        quality: 1,
        base64: true,
        });

        
        if (!result.cancelled) {
            // console.log('result.url', result.uri);
             setImage(result.uri);

            // setTitle('xxx');
            // setCever(result.uri);
            // newBook();
        
            let localUri = result.uri;
            let filename = localUri.split('/').pop();
            // Infer the type of the image
            let match = /\.(\w+)$/.exec(filename);
            let type = match ? `image/${match[1]}` : `image`;
              
            console.log('type:', type);

            const uploadData = new FormData();
            uploadData.append('title', 'lan3');
            
            uploadData.append('cover', result.uri);
            //uploadData.append('cover', { uri: localUri, name: filename, type });

            fetch('http://127.0.0.1:8000/books/', {
            method: 'POST',
            body: uploadData
            })
            .then( res => console.log('res:', res))
            .catch(error => console.log(error))
        
        }
            
            //console.log('helllo:', result);
        };
        


  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>  
        {/* <TextInput
        onChangeText={(evt) => setTitle(evt.target.value)}
        value={title}
        /> */}
      <Button title="Pick an image from camera roll" onPress={pickImage} />
      {image && <Image source={{ uri: image }} style={{ width: 200, height: 200 }} />}
    </View>
  );
};
