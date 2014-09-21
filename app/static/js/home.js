/** @jsx React.DOM */

var OrgListRow = React.createClass({
    render: function() {
        console.log(this.props);
        return (<li class="org">{this.props.org.name}</li>);
    }
});

var OrgList = React.createClass({
    render: function() {
        var orgs = [];
        this.props.orgs.forEach(function(org) {
            orgs.push(<OrgListRow org={org} key={org.name} />);
        });
        return (
            <div>
                <h2>organizations</h2>
                <ul>{orgs}</ul>
            </div>
        );
    }
});

var ORGS = [
  { name: 'usc-csci104-fall2014' },
  { name: 'usc-csci104-spring2014' }
];
 
React.renderComponent(<OrgList orgs={ORGS} />, $('#left_container')[0]);
