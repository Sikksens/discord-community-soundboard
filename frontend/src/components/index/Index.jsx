import React, {Component} from 'react';
import {connect} from 'react-redux';
import { changeMode } from './../../actions.js'
import { Redirect } from "react-router-dom";



export class IndexContainer extends Component {
	
	constructor(props) {
		super(props);
	}


	render() {		

		// Check if we are authenticated, redirect to auth otherwise
		if (this.props.authToken){
			return <Redirect to={"/bot"} />
		}
		else{
			return <Redirect to={"/auth"} />
			
		}
	}

}


const mapStateToProps = (state) => ({
	authToken: state.currentInformation.authToken
});

const mapDispatchToProps = (dispatch) => ({
	next: () => {
	
	},
});

const Index = connect(
	mapStateToProps,
	mapDispatchToProps
)(IndexContainer);

export default Index;