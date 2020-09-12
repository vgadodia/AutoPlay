import React from 'react';
import { StyleSheet, Text, View, Image, Button, ScrollView} from 'react-native';
import { AppLoading } from 'expo';
import * as Font from 'expo-font';

import SongList from "../components/songList";

let customFonts  = {
  'FuturaH': require('../assets/fonts/futurah.ttf'),
  'FuturaL': require('../assets/fonts/futural.ttf'),
};

export default class Spotify extends React.Component  {
  state = {
    fontsLoaded: false,
    playing: false,
  };

  async _loadFontsAsync() {
    await Font.loadAsync(customFonts);
    this.setState({ fontsLoaded: true });
  }

  componentDidMount() {
    this._loadFontsAsync();
  }
  getData() {
    return  [
    {
      
    name:"Evergreen",
    album:"https://pbs.twimg.com/media/Dvh-pU0XgAE1dpU.jpg", 
    artist:"Painted West",
  },
  {
    
    name:"Evergreen",
    album:"https://pbs.twimg.com/media/Dvh-pU0XgAE1dpU.jpg", 
    artist:"Painted West",
  },
  {
    
    name:"Evergreen",
    album:"https://pbs.twimg.com/media/Dvh-pU0XgAE1dpU.jpg", 
    artist:"Painted West",
  },
  ]
  }

  render(){
    if (this.state.fontsLoaded) {
    return (
    <View style={styles.container}>
      <Image source={require('../assets/settings.png')} style={styles.left}></Image>
      <Image source={require('../assets/help.png')} style={styles.right}></Image>
      <View style={styles.playing}>
          {this.state.playing &&
          <View>
            <Text style={{position:'relative',fontSize:20,marginTop:'20%',textAlign:'center', color:'#364f6b', fontFamily:'FuturaH'}}>Currently not playing</Text>
            <Image source={require('../assets/404.png')} style={styles.middle}></Image>
          </View>
    }
    {!this.state.playing &&
          <View>
            <Text style={{position:'relative',fontSize:20,marginTop:'10%',textAlign:'center', color:'#364f6b', fontFamily:'FuturaH'}}>Currently playing</Text>
            <Image source={require('../assets/album.png')} style={styles.album}></Image>
            <Text style={{position:'relative',fontSize:15,marginTop:'5%',textAlign:'center', color:'#364f6b', fontFamily:'FuturaH'}}>Old Town Road</Text>
            <Text style={{position:'relative',fontSize:15,marginTop:'2%',textAlign:'center', color:'#364f6b', fontFamily:'FuturaL'}}>Lil Nas X</Text>
            <View style={{flex:1, flexDirection:'row', marginTop:'5%', alignSelf:'center'}}><Image source={require('../assets/spotify.png')} style={styles.spotify}></Image>
            <Text style={{position:'relative',fontSize:15,marginTop:'2%',textAlign:'center', color:'#FFF', fontFamily:'FuturaH', backgroundColor:'#1F1F1F', marginLeft:'-10%',padding:'2%',paddingLeft:'10%', width:'60%',height:30,borderRadius:10}}>Open with Spotify</Text>
            </View>
          </View>
    }
      </View>
      <Text style={{position:'relative',fontSize:20,marginTop:'10%',marginLeft:'5%', textAlign:'left', color:'#364f6b', fontFamily:'FuturaH'}}>Previously played</Text>
    
      <ScrollView style={styles.scrollcontainer}>
      <SongList itemList={this.getData()}/>
      </ScrollView>
      
      
    </View>
    );
    }
    else {
    return <AppLoading />;
    }
  }
}

const styles = StyleSheet.create({
  container: {
    height:'100%',
    position:'relative',
    backgroundColor:'#f5f5f5'
  },
  left:{
    height:'7%',
    width:'7%',
    top:'2.5%',
    resizeMode:'contain',
    left:'5%',
    position:'absolute',
  },
  right:{
    height:'7%',
    width:'7%',
    top:'2.5%',
    resizeMode:'contain',
    right:'5%',
    position:'absolute'
  },
  middle:{
    height:'60%',
    width:'60%',
    marginTop:'5%',
    resizeMode:'contain',
    zIndex:3,
    alignSelf:'center',
  },
  album:{
    height:'40%',
    width:'50%',
    marginTop:'7.5%',
    resizeMode:'contain',
    zIndex:3,
    alignSelf:'center',
  },
  spotify:{
    height:'100%',
    width:'8%',
    marginTop:'7.5%',
    resizeMode:'contain',
    zIndex:3,
    alignSelf:'center',
    marginLeft:'2%',
  },
  playing:{
      width:'70%',
      height:'40%',
      elevation:1,
      backgroundColor:'#FFF',
      alignSelf:'center',
      marginTop:'15%',
      borderRadius:20
  }
  
});