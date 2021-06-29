const chai  = require(`chai`);
const mocha  = require(`mocha`);

const app = require(`../app.js`);
const expect = chai.expect;

const minA = -8, minPlusA = minA+1, minMinusA = minA-1;
const maxA = 10, maxPlusA = maxA+1, maxMinusA = maxA-1;
const minB = -7, minPlusB = minB+1, minMinusB = minB-1;
const maxB = 5, maxPlusB = maxB+1, maxMinusB = maxB-1;
const nominalA = Math.ceil((minA+maxA)/2), nominalB = Math.ceil((minB+maxB)/2);

describe(`Integral of x(Robust Testing)[A ==> [-8, 10]    B ==> [-7, 5]]`, () => {
	it(`Test ${nominalA} and ${nominalB}(nominal and nominalB)`, ()=>{
		let res = app.x_intergral(nominalA,nominalB);
		expect(res).to.equal((nominalA**2 + nominalB**2)/2);
	});
	it(`Test ${nominalA} and ${minB}(nominalA and minB)`, ()=>{
		let res = app.x_intergral(nominalA,minB);
		expect(res).to.equal((nominalA**2 - minB**2)/2);
	});
	it(`Test ${nominalA} and ${maxB}(nominal and maxB)`, ()=>{
		let res = app.x_intergral(nominalA,maxB);
		expect(res).to.equal((nominalA**2 - maxB**2)/2);
	});
	it(`Test ${nominalA} and ${minPlusB}(nomailA and minPlusB)`, ()=>{
		let res = app.x_intergral(nominalA,minPlusB);
		expect(res).to.equal((nominalA**2 - minPlusB**2)/2);
	});
	it(`Test ${nominalA} and ${maxPlusB}(nominalA and maxPlusB)`, ()=>{
		let res = app.x_intergral(nominalA,maxPlusB);
		expect(res).to.equal((nominalA**2 - maxPlusB**2)/2);
	});
	it(`Test ${nominalA} and ${minMinusB}(nominalA and minMinusB)`, ()=>{
		let res = app.x_intergral(nominalA,minMinusB);
		expect(res).to.equal((nominalA**2 - minMinusB**2)/2);
	});
	it(`Test ${nominalA} and ${maxMinusB}(nominalA and maxMinusB)`, ()=>{
		let res = app.x_intergral(nominalA,maxMinusB);
		expect(res).to.equal((nominalA**2 - maxMinusB**2)/2);
	});
	it(`Test ${minA} and ${nominalB}(minA and nominalB)`, ()=>{
		let res = app.x_intergral(minA,nominalB);
		expect(res).to.equal((minA**2 - nominalB**2)/2);
	});
	it(`Test ${maxA} and ${nominalB}(maxA and nominalB)`, ()=>{
		let res = app.x_intergral(maxA,nominalB);
		expect(res).to.equal((maxA**2 - nominalB**2)/2);
	});
	it(`Test ${minPlusA} and ${nominalB}(minPlusA and nominalB)`, ()=>{
		let res = app.x_intergral(minPlusA,nominalB);
		expect(res).to.equal((minPlusA**2 - nominalB**2)/2);
	});
	it(`Test ${maxPlusA} and ${nominalB}(maxPlusA and nominalB)`, ()=>{
		let res = app.x_intergral(maxPlusA,nominalB);
		expect(res).to.equal((maxPlusA**2 - nominalB**2)/2);
	});
	it(`Test ${minMinusA} and ${nominalB}(minMinusA and nominalB)`, ()=>{
		let res = app.x_intergral(minMinusA,nominalB);
		expect(res).to.equal((minMinusA**2 - nominalB**2)/2);
	});
	it(`Test ${maxMinusA} and ${nominalB}(maxMinusA and nominalB)`, ()=>{
		let res = app.x_intergral(maxMinusA,nominalB);
		expect(res).to.equal((maxMinusA**2 - nominalB**2)/2);
	});
});
