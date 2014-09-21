/** @jsx React.DOM */

var OrgListRow = React.createClass({displayName: 'OrgListRow',
    render: function() {
        console.log(this.props);
        return (React.DOM.li({class: "org"}, this.props.org.name));
    }
});

var OrgList = React.createClass({displayName: 'OrgList',
    render: function() {
        var orgs = [];
        this.props.orgs.forEach(function(org) {
            orgs.push(OrgListRow({org: org, key: org.name}));
        });
        return (
            React.DOM.div(null, 
                React.DOM.h2(null, "organizations"), 
                React.DOM.ul(null, orgs)
            )
        );
    }
});

var ORGS = [
  { name: 'usc-csci104-fall2014' },
  { name: 'usc-csci104-spring2014' }
];
 
React.renderComponent(OrgList({orgs: ORGS}), $('#left_container')[0]);
